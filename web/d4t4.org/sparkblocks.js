outputToUser="";

function renderNumbers(numbers)
{
    var base=9601;
    var range=6;
    // permitted unicode decimal values go from base to base+range
    // so there are (range+1) permitted values

    var result="";

    var minValue = numbers[0];
    var maxValue = numbers[0];
    for (i=1; i<numbers.length; i++) {
        minValue = Math.min(minValue, numbers[i]);
        maxValue = Math.max(maxValue, numbers[i]);
    }
    var valueScale = maxValue - minValue;


    for (i=0; i<numbers.length; i++) {
        scaledValue = (numbers[i] - minValue) / valueScale;  // scaledValue is a real value in [0,1]
	num=Math.floor(Math.min(range, scaledValue * (range+1))); // num is now an integer value in [0, range]

	// sadly, unicode 9604 and 9608 dont render properly in my browser.
	// they are not vertically aligned the same as the other unicode block elements
	// so it looks crap.
	//
	// thus we hack.
	//
        if (num == 3) {
	    if (scaledValue * (range+1) < 3.5) { num = 2 } else { num = 4 }
	}
	if (num == 7) { num = 6 }

	outputToUser=outputToUser+"["+numbers[i]+":"+scaledValue+":"+num+"], ";
        result+=String.fromCharCode(base+num);
    }
    return result;
}

function randomBlock()
{
// never return 3 or 7, they doesnt align properly
  answer = Math.floor(6 * Math.random());
  if (answer == 3) return randomBlock();  // we takes our chances on a stack blowout.  feel lucky?
  return answer;
}

function randomBlocks()
{
    var base=9601;
    var result="";
    for (i=0; i<20; i++) {

        result+=String.fromCharCode(base+randomBlock());
    }
    return result;
}

function redraw()
{
    // get the user input and get an array of the numbers in it
    var userinput=document.getElementById("userinput").value;

    if (!userinput) {
      document.getElementById("demo").innerHTML="▇▆▆▇▇▇▇▅▂▁▁▂";
      return;
    }


    var userNumbers = userinput.match(/-?\d+\.?\d*/g) || "";


    outputToUser = "";

    // resample the series to the desired number of characters
    // we have X > C data points and we want to output not more than C characters.
    //
    // So the first character will be based on the average of the
    // first ceil(X/C) data points.
    var maxOutLength = document.getElementById("range").innerHTML;
    var outputLength = Math.min(userNumbers.length, maxOutLength);
    var outputNumbers = [outputLength];

    var chunkSize = Math.ceil(userNumbers.length / outputLength);
    var sumValues = 0;
    var sumCount = 0;
    var chunkNum = 0;
    for (i=0; i<userNumbers.length; i++) {
	sumValues += parseFloat(userNumbers[i]);
	sumCount++;
	if (sumCount == chunkSize || i == (userNumbers.length - 1)) {
	    outputNumbers[chunkNum] = sumValues / sumCount;
	    chunkNum++;
	    sumValues = 0;
	    sumCount = 0;
	}
    }


    result = renderNumbers(outputNumbers);

    // only for debugging
    //    document.getElementById("numbers").innerHTML=outputToUser;

    document.getElementById("demo").innerHTML=result;
}

function showValue(newValue)
{
document.getElementById("range").innerHTML=newValue;
redraw();
}

function init() {
// document.getElementById("demo").innerHTML="Example: " + randomBlocks();
// document.getElementById("userinput").focus();
}

if(window.attachEvent) {
    window.attachEvent('onload', init);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function() {
            curronload();
            init();
        };
        window.onload = newonload;
    } else {
        window.onload = init;
    }
}

//   document.addEventListener;
//   document.addEventListener('load',init,false):
//   document.attachEvent('onload',init);

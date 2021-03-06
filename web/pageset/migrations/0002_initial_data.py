# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        pageset = orm.Pageset(name='datacollective',
            template_name='pageset/datacollective.html')
        pageset.save()

        for i in range(len(PAGES)):
            page_data = dict(PAGES[i])
            page_data.setdefault('order', i)
            page_data.setdefault('pageset', pageset)
            page = orm.Page(**page_data)
            page.save()

    def backwards(self, orm):
        orm.Pageset.objects.all().delete()
        orm.Page.objects.all().delete()

    models = {
        'pageset.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'pageset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pageset.PageSet']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pageset.pageset': {
            'Meta': {'object_name': 'PageSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pageset']

PAGES = [{'title': 'Tweetable Sparkblocks',
          'short_title': 'Sparkblocks',
          'filename': 'sparkblocks.html',
          'content':
"""<script type="text/javascript">
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
    var userNumbers = userinput.match(/-?\d+\.?\d*/g);
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
document.getElementById("demo").innerHTML="Example: " + randomBlocks();
document.getElementById("userinput").focus();
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

</script>

<div id='wsite-content'>
    <div  class="paragraph editable-text" style=" text-align: left; ">
        <strong>
        1. Paste numbers here.
        <INPUT TYPE=TEXT NAME="fahr" id="userinput" SIZE=30 ONKEYUP="redraw()">
        <br><br>
        2. At most, how long do you want your sparkblock to be (in characters)?
        <input type="range" min="5" max="50" value="10" step="1" onchange="showValue(this.value)" />
        <span id="range">10</span>

        <p>3. Copy and paste the following blocks into a tweet, email, or anyplace else. Extra points for creativity!</p>
        <br>
        <p id="demo"></p>
        <br>
        <small><small>Inspired by Alex Kerin's <a href="http://www.datadrivenconsulting.com/2010/06/twitter-sparkline-generator/">Twitter Sparkline Generator</a>
        <br>
        Feedback to dsjoerg@datacollective.org</small></small>

<br><br>
<!--
DEBUGGING: <p id="numbers">Numbers are going to be here.</p>
-->
</strong>""",
    },
    {'title': 'Discuss',
     'filename': 'discuss.html',
     'content':
     """<div  class="paragraph editable-text" style=" text-align: left; ">
    <strong>We are discussing the Data Collective in a
     <a href="http://groups.google.com/forum/#!forum/datacollective" target="_blank" title="">forum on Google Groups</a>.<br /><br />
     We'd love to hear your ideas, please join in!</strong></div>""",
    },
    {'title': 'Join Us',
     'filename': 'join-us.html',
     'content':
"""<div  class="paragraph editable-text" style=" text-align: left; ">
<strong>We're assembling a small elite team.<br /><br />
One hacker, one interface/community wizard and a writer-analyst.
<br /><br />We're ambitious but not crazy -- this thing can really work.&nbsp;
Some similar services are described and briefly
analyzed&nbsp;<a href="http://bit.ly/lLm73I" target="_blank" title="">here</a>.
<br /><br />
To apply or learn more, email dsjoerg@datacollective.org.</strong></div>""",
     },
    {'title': 'Home',
     'filename': 'index.html',
     'content':
"""<h2  style=" text-align: left; "><font size="4">Public data is impossible to use.</font></h2>
<div  class="paragraph editable-text" style=" text-align: left; display: block; "><font size="3"><strong><br />We're going to fix it.<br /><br /><span style="line-height: 20px; ">In ten seconds, you can find out who was the guest star on "30 Rock" last week.</span><br /><br /><span style="line-height: 20px; ">How long does it take you to find historical charts and data for:</span><br /><span style="line-height: 20px; ">* income inequality</span><br /><span style="line-height: 20px; ">* government tax and spending</span><br /><span style="line-height: 20px; ">* global temperature trends</span><br /><br /><span style="line-height: 20px; ">And do you trust the results once you find them?</span><br /><br /><span style="line-height: 20px; ">Our ultimate goal: nudge public discourse in the direction of the facts.</span></strong></font>
""",
    },
    #{'title': 'test',
    # 'filename': 'test.html',
    # 'content': 'this is a test',
    # },
]

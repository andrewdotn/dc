/*
	Class for managing the comment form used for threaded replies.
*/
function CommentReplyForm(template) {
	this.template = template;
}
CommentReplyForm.preparetemplate = function(id) {
	// This is dependent on the markup the view creates.
	var template = $(document.getElementById(id)).clone();
	template.find('.error').empty();
	template = template.removeAttr('id'); // remove the id attribute
	template.children('h2').text('Reply to Comment'); // Change header
	template.addClass('reply'); // styling hook
	return template;
}
CommentReplyForm.prototype.show = function(parentcommentid) {
	this.template.find('form input.comment_parentnumber').val(parentcommentid);
	this.template.attr('style','display:none');
	$('#comment_'+parentcommentid).append(this.template);
	this.template.removeAttr('style');
	var button = this.template.prevAll('button.comment_reply');
	if (button.length) {
		button.data('replytext', button.text());
		button.text('cancel reply')
		.get(0).comment_formopen=true;
	}
};

CommentReplyForm.prototype.hide = function() {
	this.template.attr('style','display:none');
	this.template.find('form input.comment_parentnumber').val('');
	var button = this.template.prevAll('button.comment_reply');
	if (button.length) {
		button.text(button.data('replytext'))
		.get(0).comment_formopen=false;
	}
};
CommentReplyForm.prototype.getCurrentParentId = function(self) {
	return self.template.find('form input.comment_parentnumber').val();
};
CommentReplyForm.prototype.replyButtonHandler = function(e) {
	var self = e.data.self;
	if (e.target.comment_formopen) {
		self.hide();
	} else {
		var currentparentcommentid = self.getCurrentParentId(self);
		// IE 6/7 have a button element bug where 'value' is always overwritten
		// with .textContent
		// Below is the only way to get the real value attribute value in IE.
		// Even .getAttribute('value') doesn't work.
		// I don't think this method is available in IE5.5, so they're out of luck
		var parentcommentid = e.target.getAttributeNode('value').nodeValue;
		if (parentcommentid!=currentparentcommentid) {
			if (currentparentcommentid!==null) {
				self.hide();
			}
			self.show(parentcommentid);
		}
	}
};
CommentReplyForm.prototype.bindHandlers = function(replybuttons) {
	var data = {self:this};
	$(replybuttons).bind('click', data, this.replyButtonHandler);
};

var CommentPreview = {};
CommentPreview.previewResponseHandler = function(commentform, data, textStatus) {
	var preview = commentform.find('div.commentpreview');
	preview.empty();
	if (textStatus==='error') {
		preview.append('<span class="error">Unable to retrieve preview</span>').fadeIn();
	} else {
		preview.append(data).fadeIn();
	}
};
CommentPreview.previewButtonHandler = function(e) {
	var commentform = e.data.commentform;
	var responsecallback = function(data, textStatus) {
		CommentPreview.previewResponseHandler(commentform, data, textStatus);
	};
	commentform.find('div.commentpreview').fadeOut();
	$.ajax({
		url : e.data.previewurl,
		type : 'POST',
		dataType : 'html',
		data : e.data.commentform.find('form').serialize(),
		success : responsecallback,
		error : responsecallback
	});
};
CommentPreview.bindHandlers = function(commentform, previewbutton, previewurl) {
	var data = {commentform:commentform, previewurl:previewurl};
	$(previewbutton).bind('click', data, CommentPreview.previewButtonHandler).show();
};

$(function(){
	var template = CommentReplyForm.preparetemplate('commentform');
	var crf = new CommentReplyForm(template);
	crf.bindHandlers('div.com-block button.comment_reply');
	var previewurl = $('#commentform form').attr('action').replace(/\/post$/, '/preview');
	CommentPreview.bindHandlers(template, template.find(':button.preview'), previewurl);
	CommentPreview.bindHandlers($('#commentform'), $('#commentform :button.preview'), previewurl);
});

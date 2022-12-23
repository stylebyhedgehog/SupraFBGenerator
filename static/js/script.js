$(".copyBtn").click(function(){
    selector = "#"+$(this).attr('id')+"_text"
    $(selector).select()
   
    document.execCommand('copy');
});
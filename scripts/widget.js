(function() {  
    var jQuery;  
    if (window.jQuery === undefined || window.jQuery.fn.jquery !== '1.9.1') {     
        var script_tag = document.createElement('script');     
        script_tag.setAttribute("type","text/javascript");     
        script_tag.setAttribute("src","http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js");
        if (script_tag.readyState) {       
            script_tag.onreadystatechange = function () { 
                if (this.readyState == 'complete' || this.readyState == 'loaded') {               
                    scriptLoadHandler();           
                }       
            };     
        } else { 
            script_tag.onload = scriptLoadHandler;     
        }     
        (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag); 
    } else {     
        jQuery = window.jQuery;     
        main(); 
    }  
    function scriptLoadHandler() {     
        jQuery = window.jQuery.noConflict(true);     
        main();  
    }  
    function main() {      
        jQuery(document).ready(function($) {          
            //var css_link = $("<link>", {              
            //    rel: "stylesheet",              
            //    type: "text/css",              
            //    href: "style.css"          
            //});         
            //css_link.appendTo('head');                    
            var json_url = "http://127.0.0.1:8084/loadData"
            $.ajax({
                url: json_url,
                async: false,
                dataType: 'json',
                success: function(data) {
                    $('#widget').html("Response: " + data.response);
                }
            });
        });
    }  
})(); 

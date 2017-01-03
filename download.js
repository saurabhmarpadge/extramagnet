var page = require('webpage').create();
var fs = require('fs');
var system = require('system');
var args = system.args;
var output = 'html_page.html';  
page.open('http://extratorrent.cc/search/?search='+args[1]+'&s_cat=4&pp=10&srt=seeds&order=desc', function() { // open the file 
  fs.write(output,page.content,'w'); 
  phantom.exit(); 
});

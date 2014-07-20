/*
 * Copyright (c) 2009 Katie Capps Parlante
 */

function slideAnimation(element, callback) {
	var divHeightPx = element.css("height");
	var divHeight = element.height();
	var newTop = divHeight + 100;
	
	element.css({opacity:1.0, height:0, top:newTop});
    element
		.animate({height:divHeight, top:100}, "slow")
		.animate({opacity:1.0}, 2000)
		.animate({height:0}, "slow", function(){
			$('.stanza').css({opacity:0.0, height:divHeightPx, top:100});
			callback();
		});
}

function sideways(element, callback) {
    var firstLine = element.find('div:eq(0)');
    var secondLine = element.find('div:eq(1)');
    var thirdLine = element.find('div:eq(2)');

    var elementWidth = element.width();
    var firstLineWidth = firstLine.width();
    var secondLineWidth = secondLine.width();
    var thirdLineWidth = thirdLine.width();

    firstLine.css({marginLeft:-firstLineWidth});
    secondLine.css({marginLeft:elementWidth});
    thirdLine.css({marginLeft:-thirdLineWidth});
    element.css({opacity:1});

    firstLine.animate({marginLeft:0}, 1500, function(){
        secondLine.animate({opacity:1}).animate({marginLeft:0}, 1500, function(){
            thirdLine.animate({opacity:1}).animate({marginLeft:0}, 1500).animate({opacity:1}, 3000, function() {
            	firstLine.animate({marginLeft:elementWidth}, 1500, function(){
    				secondLine.animate({opacity:1}).animate({marginLeft:-secondLineWidth}, 1500, function(){
    					thirdLine.animate({opacity:1}).animate({marginLeft:elementWidth}, 1500, callback);
    				});
    			});
    		});
        });
    });		


}

function fadeSearchAnimation(element, callback) {
	element
		.fadeIn("slow")
		.animate({opacity:1.0}, 3000, function(){
			$(this).find('.search')
			.animate({opacity:0}, 3000, function(){
				$(this).parent().find('.tweet')
				.animate({opacity:1.0}, 3000, function(){
					$(this).animate({opacity:0}, "slow", function(){
						if ($(this)[0] === $('.tweet:last')[0]) {
							callback();
						}
					});
				});
			});
		});
}
	
function dropAnimation(element, callback) {
	element.fadeIn("slow")
		.animate({opacity:1.0}, 2000)
		.animate({
			opacity:0,
			top: $(window).height() - element.height()
		}, "slow", callback);
}

function spantext(phrase) {
	var newtext = "";
	
	// Made search global so it searches and replaces all
	phrase = phrase.replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
	
	//phrase = phrase.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'");
	for (var i=0; i < phrase.length; i++) {
	    if (phrase.charAt(i) != ' ') {
		    newtext = newtext.concat("<span class='letter'>" + phrase.charAt(i) + "</span>");
		} else {
		    newtext = newtext.concat(" ");
		}
	}
	return newtext;
}

function fadeLetter(element, callback) {
	var line = element.find('div:eq(3) .tweet');
	var html = line.html();
	
	line.html(spantext(html));
	
	var seconds = 0;
	
	element.animate({opacity:1.0}, "slow")
		.animate({opacity:1.0}, 2000, function(){
			$(this).find("span.letter").animate({opacity:1.0}, 5, function(){
				seconds = 100 + Math.floor(Math.random() * 3000);
				$(this).animate({opacity:1.0}, seconds).animate({opacity:0}, "slow")
			});
			$(this).animate({opacity:1.0}, 4000).animate({opacity:0}, "slow", function(){
				line.html(html);
				callback();
			});
		});
}

function projectionAnimation(element, callback) {
	
	//Dynamically calculate width/height of poem
	//Set margins accordingly to center poem
		
	// Mapping fontSize to "length" of poem as measured by its width at 64px font.
	var width = element.width();
	if (width < 500)
		width = 500;
	var fontSize = 128 - (((width-500)/1600)*48);
	
	
	$('.stanza').css('font-size', fontSize);
	
	var newWidth = element.width();
	

	if(newWidth > 1700)
		newWidth = 1700;

	console.log("Width: " + width.toString() + "\t" + "New Width: " + newWidth.toString() + "\t" + "Font Size: " + fontSize.toString());

	$('#poem').css({
		'width' : newWidth,
		'overflow' : 'hidden',
		'margin-left' : leftMargin,
		'margin-top'  : $(document).height()*.33,	
	});
		

	$('#poem').find('.phrase').css('white-space','nowrap');
    
    element.find('.tweet, .search').each(function(){
        var html = $(this).html();
        
        $(this).data("old", html);
        $(this).html(spantext(html));
    });
    
    var seconds = 0;
    var holdLength = 10000;
    
    element.find("span.letter").css({opacity:0});
    element.css({opacity:1, 'display':'block'});
    
    element.find("span.letter").each(function(){
        seconds = 100 + Math.floor(Math.random() * 3000);
        $(this).animate({opacity:0}, seconds).animate({opacity:1.0}, "slow")
    });

    element.animate({opacity:1.0}, 6000, function() {
        $(this).find("span.letter").animate({opacity:1.0}, 4000, function(){
            seconds = 100 + Math.floor(Math.random() * 3000);
            $(this).animate({opacity:1.0}, seconds).animate({opacity:1.0}, holdLength).animate({opacity:0}, "slow")
        });
		$(this).animate({opacity:1.0}, 8000).animate({opacity:1.0}, holdLength).animate({opacity:0}, "slow", function(){
			element.find('.tweet, .search').each(function(){
				var old = $(this).data("old");
				$(this).html(old);
			});
			callback();
		});
    });
}

function fountain(element, callback) {
    
    $('#poem').css({
        'width' : element.width(),
    });

    $('#poem').find('.phrase').css('white-space','nowrap');
    // TODO: reconsider above
  
    element.find('.tweet, .search').each(function(){
        var html = $(this).html();
        
        $(this).data("old", html);
        $(this).html(spantext(html));
    });
    
    var seconds = 0;
    
    element.find("span.letter").css({opacity:0});
    element.css({opacity:1, 'display':'block'});
    
    element.find("span.letter").each(function(){
        seconds = 100 + Math.floor(Math.random() * 3000);
        $(this).animate({opacity:0}, seconds).animate({opacity:1.0}, "slow")
    });

    element.animate({opacity:1.0}, 6000, function() {
        $(this).find("span.letter").animate({opacity:1.0}, 4000, function(){
            seconds = 100 + Math.floor(Math.random() * 3000);
            $(this).animate({opacity:1.0}, seconds).animate({opacity:0}, "slow")
        });
        $(this).animate({opacity:1.0}, 8000).animate({opacity:0}, "slow", function(){
            element.find('.tweet, .search').each(function(){
              var old = $(this).data("old");
              $(this).html(old);
            });
            callback();
        });
    });
}


function fadeLines(element, callback) {
    var firstLine = element.find('div:eq(0)');
    var secondLine = element.find('div:eq(1)');
    var thirdLine = element.find('div:eq(2)');
    
    firstLine.css({opacity:0});
    secondLine.css({opacity:0});
    thirdLine.css({opacity:0});
    element.css({opacity:1});
    
    firstLine.animate({opacity:1.0}, "slow", function(){
        secondLine.animate({opacity:0}).animate({opacity:1.0}, "slow", function(){
            thirdLine.animate({opacity:0}).animate({opacity:1.0}, "slow").animate({opacity:1}, 2000, function() {
            	firstLine.animate({opacity:0}, "slow", function(){
    				secondLine.animate({opacity:1}).animate({opacity:0}, "slow", function(){
    					thirdLine.animate({opacity:1}).animate({opacity:0}, "slow", callback)
    				});
    			});
    		});
        });
    });		
}

function fadePair(element, callback) {
    var firstLine = element.find('div.line1');
    var secondLine = element.find('div.line2');
    
    firstLine.css({opacity:0});
    secondLine.css({opacity:0});
    element.css({opacity:1});
    
    firstLine.animate({opacity:1.0}, "slow", function(){
        secondLine.animate({opacity:0}).animate({opacity:1.0}, "slow").animate({opacity:1}, 4000, function() {
            firstLine.animate({opacity:0}, "slow", function(){
    			secondLine.animate({opacity:1}).animate({opacity:0}, "slow", callback)
    		});
        });
    });		
    
}


function cycle(animation) {
	if ($('div').length > 0) {
	    animation($('div:first'), function() {
            $('div:first').remove();
            cycle(animation);
        });
	} else {
		$('body').load('/tweets/', function() {
			$('.stanza').css({opacity:0});
			cycle(animation);
		});
	}
}

function cycleCustom(animation, search_one, search_two, search_three, page) {
	if ($('div').length > 0) {
	    animation($('div:first'), function() {
            $('div:first').remove();
            cycleCustom(animation, search_one, search_two, search_three, page);
        });
	} else {
	    var query = "?one=" + search_one + "&two=" + search_two + "&three=" + search_three + "&page=" + page
	    page += 1;
		$('body').load('/lines/' + query, function() {
			$('.stanza').css({opacity:0});
			cycleCustom(animation, search_one, search_two, search_three, page);
		});
	}
}

function fadeInOut(element) {
	element.fadeIn(10000, function(){
		element.fadeOut(5000, function(){
			fadeInOut(element);
		})
	})
}

function cycleRandom(title, animation, page) {
	if ($('div.stanza').length > 0) {
	    animation($('div.stanza:first'), function() {
            $('div.stanza:first').remove();
            cycleRandom(title, animation, page);
        });
	} else {
		var loading = $("<div>").attr("id", "loading").text("...Collecting Tweets...").prependTo($("body"));
		fadeInOut(loading);
	    if (page === 1000) return;
	    var query = "?page=" + page;
	    page += 1;
		$('#poem').load('/' + title + '.html' + query, function(responseText, textStatus) {
			$('div.stanza').css({opacity:0, 'display':'none'});
			loading.fadeOut("fast", function(){ loading.remove(); });
			cycleRandom(title, animation, page);
		});
	}
    
}

function cycleSelect(animation) {
	if ($('div.stanza').length > 0) {
	    animation($('div.stanza:first'), function() {
            $('div.stanza:first').remove();
            cycleSelect(animation);
        });
	} else {
		var loading = $("<div>").attr("id", "loading").text("Select Poems...").prependTo($("body"));
		fadeInOut(loading);
		setTimeout(function(){
			$('#poem').load('/select.html', function(responseText, textStatus) {
				$('div.stanza').css({opacity:0, 'display':'none'});
				loading.fadeOut("fast", function(){ loading.remove(); });
				cycleSelect(animation);
			});
		}, 2500)
	}
    
}

function fadeHeadline(tag, dates, url, callback) {
  var headline = $('#headline');
  var tag = $("<div>").attr("id", "#tag").text(tag).append($("<div>").attr("id", "#dates").text(dates).css('font-size', '60px'));
  var url = $("<div>").attr("id", "#url").text(url);
  
  headline
  	.append(tag)
  	.append(url);
  
  headline.show();
  headline.css('opacity', 0);
  headline.animate({ opacity: .99 }, 8000, function(){
	  setTimeout( function(){ 
		  tag.animate({ opacity: .01 },3000);
		  url.fadeOut(8000, function(){
			  headline.empty();
			  headline.hide();
			  setTimeout(callback, 2000);
	  		});
	  	}, 5000);
  	});
}

function cycleProjection(title, animation, page) {

  if ($('div.stanza').length > 0) {
	    animation($('div.stanza:first'), function() {
            $('div.stanza:first').remove();
            cycleProjection(title, animation, page);
        });
	} else {
	
    if (page === 1000) return;

    // Get poems in batches of 15
    var query = "?size=15&page=" + page;
    var newtitle = "";
    if (title == "transit") {
        newtitle = "aspiration";
      } else if (title == "aspiration") {
        newtitle = "contemplation";
      } else if (title == "contemplation") {
        newtitle = "transit";
        page += 1;
      }
        
    // Show tagline for every batch of poems
		$("#subtitle").fadeOut("fast", function(){
	    	fadeHeadline("3 Strangers. 3 Tweets. 1 Accidental Poem.", "Fri/Sat nights thru Oct 13", "multivers.es", function() {
	    		$("#subtitle").fadeIn("slow", function(){
	    			$('#poem').load('/' + title + '.html' + query, function(responseText, textStatus) {
	                    $('div.stanza').css({opacity:0, 'display':'none'});
	                    cycleProjection(newtitle, animation, page);
	                  });
	    			});	    		
	    		});
			});
    	}
}



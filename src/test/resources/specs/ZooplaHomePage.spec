@objects
   header-nav             xpath         //*[@id="main-header"]
   header-logo            xpath         //*[@id="logo"]
   header-Myenquiries     xpath         //*[@id="main-nav"]/ul[1]/li[1]/a
   header-viewmyhome      xpath         //*[@id="main-nav"]/ul[1]/li[2]/a
   header-signin          xpath         //*[@id="main-nav"]/ul[1]/li[3]/a
   header-forsale         xpath         //*[@id="mn-buy"]/a
   header-torent          xpath         //*[@id="mn-rent"]/a  
   header-hoouseprices    xpath         //*[@id="mn-prices"]/a   
   header-newhomes        xpath         //*[@id="mn-new"]/a
   header-commercial      xpath         //*[@id="mn-commercial"]/a
   header-overseas        xpath         //*[@id="mn-overseas"]/a
   header-findagents      xpath         //*[@id="mn-agents"]/a
   header-discover        xpath         //*[@id="mn-advice"]/a
   sub-header-link1       xpath         //*[@id="mn-buy"]/div/ul[1]/li[1]/a
   
   
   

   
= Header =
   header-logo:
        inside screen 16px top
        visible
        width 96px
        aligned horizontally all header-Myenquiries ~24px
        inside header-nav 16px top, 255px left, 61px bottom, 1329px right
        aligned horizontally centered header-nav ~ 22px
        left-of header-Myenquiries 726px
        left-of header-viewmyhome 852px
        left-of header-signin 988px
        height 24px
        css font-weight contains "400"
        text is "Zoopla"
        css color contains "rgba(255, 255, 255, 1)"
        css font-size contains "16px"
        css font-family contains "arial, helvetica, sans-serif"
        css outline-width contains "0px"
        css text-align contains "left"
        css font-stretch contains "100%"
        css line-height is "16.224px"
        css border-bottom-left-radius contains "0px"
        css border-bottom-right-radius contains "0px"
        css border-top-right-radius contains "0px"
        css border-top-left-radius contains "0px"
        css font-stretch contains "100%"
        css padding-bottom contains "0px"
        css padding-left contains "0px"
        css padding-right contains "0px"
        css padding-top contains "0px"
        
   header-Myenquiries:
         visible
         aligned horizontally centered header-nav ~24px
         inside header-nav 12px top, 1077px left, 60px bottom, 489px right
         right-of header-logo 726px
         left-of header-viewmyhome 12px
         height ~ 29px
         text is "My enquiries"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "12px"
         css font-family contains "Lato, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "500px"
         css border-bottom-right-radius contains "500px"
         css border-top-right-radius contains "500px"
         css border-top-left-radius contains "500px"
         css font-stretch contains "100%"
         css padding-bottom contains "6px"
         css padding-left contains "18px"
         css padding-right contains "18px"
         css padding-top contains "6px"
         css text-align contains "center"
         css font-stretch contains "100%"
         css line-height is "13.2px"
         
         
   header-viewmyhome:
         visible
         aligned horizontally centered header-nav ~24px
         aligned horizontally centered header-Myenquiries ~5px
         aligned horizontally centered header-signin ~5px
         inside header-nav 12px top, 1203px left, 60px bottom, 354px right
         right-of header-logo 852px
         right-of header-Myenquiries 12px
         left-of header-signin 13px
         height ~ 29px
         text is "View my home"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "12px"
         css font-family contains "Lato, sans-serif"
         css outline-width contains "0px"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "500px"
         css border-bottom-right-radius contains "500px"
         css border-top-right-radius contains "500px"
         css border-top-left-radius contains "500px"
         css font-stretch contains "100%"
         css padding-bottom contains "6px"
         css padding-left contains "18px"
         css padding-right contains "18px"
         css padding-top contains "6px"
         css text-align contains "center"
         css font-stretch contains "100%"
         css line-height is "13.2px"
         
         
   header-signin:
         visible
         aligned horizontally centered header-nav ~24px
         aligned horizontally centered header-Myenquiries ~5px	
         aligned horizontally centered header-viewmyhome ~5px
         inside header-nav 12px top, 1339px left, 59px bottom, 255px right
         right-of header-logo 988px
         right-of header-Myenquiries 148px
         right-of header-viewmyhome 13px
         height ~ 29px
         text is "Sign in"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "13.92px"
         css font-family contains "Arial, sans-serif"
         css outline-width contains "0px"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "500px"
         css border-bottom-right-radius contains "500px"
         css border-top-right-radius contains "500px"
         css border-top-left-radius contains "500px"
         css font-stretch contains "100%"
         css padding-bottom contains "6.96px"
         css padding-left contains "20.88px"
         css padding-right contains "20.88px"
         css padding-top contains "6.96px"
         css text-align contains "center"
         css font-stretch contains "100%"
         css line-height is "normal"
         
         
   header-forsale:
         visible
         aligned vertically left header-logo ~24px
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 241px left, 8px bottom, 1356px right
         left-of header-torent 0px
         left-of header-hoouseprices 75px
         left-of header-newhomes 194px
         left-of header-commercial 304px
         left-of header-overseas 415px
         left-of header-findagents 509px
         left-of header-discover 618px
         height ~ 37px
         text is "For sale"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-torent:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 324px left, 8px bottom, 1281px right
         left-of header-hoouseprices 0px
         left-of header-newhomes 119px
         left-of header-commercial 229px
         left-of header-overseas 340px
         left-of header-findagents 434px
         left-of header-discover 543px
         height ~ 37px
         text is "To rent"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-hoouseprices:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 399px left, 8px bottom, 1162px right
         right-of header-torent 0px
         right-of header-forsale 75px
         left-of header-newhomes 0px
         left-of header-commercial 110px
         left-of header-overseas 221px
         left-of header-findagents 315px
         left-of header-discover 424px
         height ~ 37px
         text is "House prices"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-newhomes:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 518px left, 8px bottom, 1052px right
         right-of header-torent 119px
         right-of header-forsale 194px
         right-of header-hoouseprices 0px  
         left-of  header-commercial 0px
         left-of  header-overseas 111px
         left-of  header-findagents 205px
         left-of  header-discover 314px
         height ~ 37px
         text is "New homes"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-commercial:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 628px left, 8px bottom, 941px right
         right-of header-torent 229px
         right-of header-forsale 304px
         right-of header-hoouseprices 110px
         right-of header-newhomes 0px
         left-of header-overseas 0px
         left-of header-findagents 94px
         left-of header-discover 203px
         height ~ 37px
         text is "Commercial"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
   header-overseas:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 739px left, 8px bottom, 847px right
         right-of header-torent 340px
         right-of header-forsale 415px
         right-of header-hoouseprices 221px
         right-of header-newhomes 111px
         right-of header-commercial 0px
         left-of header-findagents 0px
         left-of header-discover 109px
         height ~ 37px
         text is "Overseas"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-findagents:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 833px left, 8px bottom, 738px right
         right-of header-torent 434px
         right-of header-forsale 509px
         right-of header-hoouseprices 315px
         right-of header-newhomes 205px
         right-of header-commercial 94px
         right-of header-overseas 0px
         left-of header-discover 0px
         height ~ 37px
         text is "Find agents"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
         
         
   header-discover:
         visible
         aligned horizontally centered header-torent ~5px	
         aligned horizontally centered header-hoouseprices ~5px
         inside header-nav 56px top, 942px left, 8px bottom, 650px right
         right-of header-torent 543px
         right-of header-forsale 618px
         right-of header-hoouseprices 424px
         right-of header-newhomes 314px
         right-of header-commercial 203px
         right-of header-overseas 109px
         right-of header-findagents 0px
         height ~ 37px
         text is "Discover"
         css color contains "rgba(255, 255, 255, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "400px"
         css border-bottom-right-radius contains "400px"
         css border-top-right-radius contains "400px"
         css border-top-left-radius contains "400px"
         css font-stretch contains "100%"
         css padding-bottom contains "10.4px"
         css padding-left contains "12.8px"
         css padding-right contains "12.8px"
         css padding-top contains "10.4px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "16px"
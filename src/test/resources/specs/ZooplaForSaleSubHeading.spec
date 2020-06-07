@import ZooplaHomePage.spec

@objects
   sub-header-propertyforsale                   xpath         //*[@id="mn-buy"]/div/ul[1]/li[1]/a
   sub-header-newhomesforsale                   xpath         //li[@id='mn-buy']//ul[1]//li[2]//a[1]
   sub-header-commercialpropertyforsale			xpath		  //li[@id='mn-buy']//ul[1]//li[3]//a[1]
   sub-header-estateagents			            xpath		  //li[@id='mn-buy']//li[4]//a[1]
   sub-header-Traveltimesearch			        xpath		  //*[@id="mn-buy"]/div/ul[2]/li[1]/a
   sub-header-drawamapsearch			        xpath		  //*[@id="mn-buy"]/div/ul[2]/li[2]/a
   sub-header-overseasproperty			        xpath		  //*[@id="mn-buy"]/div/ul[2]/li[3]/a
   
   
   
   
   
     
= Header = 


   sub-header-propertyforsale:
         visible
         inside header-nav 128px top, 273px left, ~40px bottom, 1265px right
         above sub-header-newhomesforsale 24px
         above sub-header-commercialpropertyforsale 65px
         height ~ 17px
         text is "UK property for sale"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         aligned vertically left sub-header-estateagents
         aligned vertically left sub-header-propertyforsale
         aligned horizontally centered sub-header-Traveltimesearch ~24px
         css background-color is "rgba(0, 0, 0, 0)"
         
         
         
   sub-header-newhomesforsale:
         visible
         inside header-nav 169px top, 273px left, -85px bottom, 1242px right
         below sub-header-propertyforsale 24px
         above sub-header-commercialpropertyforsale 24px
         aligned vertically left sub-header-propertyforsale
         aligned vertically left sub-header-propertyforsale
         aligned vertically left sub-header-estateagents
         height ~ 17px
         text is "UK new homes for sale"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         
   sub-header-commercialpropertyforsale:
         visible
         inside header-nav 210px top, 273px left, -126px bottom, 1178px right
         below sub-header-propertyforsale 65px
         below sub-header-newhomesforsale 24px
         aligned vertically left sub-header-propertyforsale
         aligned vertically left sub-header-newhomesforsale
         aligned vertically left sub-header-estateagents
         height ~ 17px
         text is "UK commercial property for sale"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"         
         
   sub-header-estateagents:
         visible
         inside header-nav 251px top, 273px left, -167px bottom, 1284px right
         below sub-header-propertyforsale 106px
         below sub-header-newhomesforsale 65px
         below sub-header-commercialpropertyforsale 24px
         aligned vertically left sub-header-propertyforsale
         aligned vertically left sub-header-commercialpropertyforsale
         aligned vertically left sub-header-newhomesforsale
         height ~ 17px
         text is "UK estate agents"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         css background-color is "rgba(0, 0, 0, 0)"
         
   sub-header-Traveltimesearch:
         visible
         inside header-nav 128px top, 652px left, -44px bottom, 897px right
         above sub-header-drawamapsearch 24px
         above sub-header-overseasproperty 65px
         aligned vertically left sub-header-drawamapsearch 65px
         aligned vertically left sub-header-overseasproperty 65px
         height ~ 17px
         text is "Travel time search"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         css background-color is "rgba(0, 0, 0, 0)"
         
   sub-header-drawamapsearch:
         visible
         inside header-nav 169px top, 652px left, -85px bottom, 890px right
         below sub-header-Traveltimesearch 24px
         above sub-header-overseasproperty 24px
         aligned vertically left sub-header-Traveltimesearch 65px
         aligned vertically left sub-header-overseasproperty 65px
         height ~ 17px
         text is "Draw a map search"
         css color contains "rgba(89, 89, 99, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         css background-color is "rgba(0, 0, 0, 0)"
         
         
   sub-header-overseasproperty:
         visible
         inside header-nav 210px top, 652px left, 840px right
         below sub-header-Traveltimesearch 65px
         below sub-header-drawamapsearch 24px
         aligned vertically left sub-header-drawamapsearch 65px
         aligned vertically left sub-header-Traveltimesearch 65px
         height ~ 17px
         text is "Overseas property for sale"
         css color contains "rgba(106, 20, 142, 1)"
         css font-size contains "16px"
         css font-family contains "arial, helvetica, sans-serif"
         css outline-width contains "0px"
         css border-bottom-left-radius contains "0px"
         css border-bottom-right-radius contains "0px"
         css border-top-right-radius contains "0px"
         css border-top-left-radius contains "0px"
         css font-stretch contains "100%"
         css padding-bottom contains "0px"
         css padding-left contains "0px"
         css padding-right contains "0px"
         css padding-top contains "0px"
         css font-stretch contains "100%"
         css text-align contains "left"
         css line-height is "25.6px"
         css background-color is "rgba(0, 0, 0, 0)"
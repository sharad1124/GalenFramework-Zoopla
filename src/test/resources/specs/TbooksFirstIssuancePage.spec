@import common.spec

@objects
   header-nav             xpath     //*[@id="main-header"]/div[1]
   header-logo            xpath    //*[@id="logo"]
   header-text-us         xpath    /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[1]/a
   header-logIn           xpath   /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[6]/a
   header-lang            xpath  //*[@id="et-top-navigation"]/div[1]/a[1]/img
   header-lang2           xpath  /html/body/div[1]/header/div[1]/div[2]/div[1]/a[2]/img
   header-solution        xpath  /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[2]
   header-pricing         xpath  /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[3]/a
   header-blog            xpath  /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[4]/a
   header-support         xpath  /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[5]/a
   header-getStarted      xpath  /html/body/div[1]/header/div[1]/div[2]/nav/ul/li[7]
   
   
= Header =

   header-logo:
        inside screen 34px top
        centered horizontally inside screen ~1322px
        visible
        width 172px
        inside header-nav 34px top, 93px left, 34px bottom, 1415px right
        aligned horizontally centered header-nav ~2px
        left-of header-text-us 572px
        left-of header-lang 457px
        left-of header-lang2 497px
        left-of header-solution 630px
        left-of header-pricing 760px
        left-of header-blog 852px
        left-of header-support 924px
        left-of header-getStarted 1103px
        
        
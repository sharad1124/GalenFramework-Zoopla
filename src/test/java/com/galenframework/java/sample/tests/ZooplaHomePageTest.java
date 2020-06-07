package com.galenframework.java.sample.tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import com.galenframework.java.sample.components.GalenTestBase;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class ZooplaHomePageTest extends GalenTestBase {  

    @Test(dataProvider = "devices",priority =1,enabled=false)
    public void Zoopla_Landing_Page_onDevice(TestDevice device) throws IOException {
        load("/");
        getDriver().findElement(By.xpath("//button[@class='ui-button-secondary']")).click();
        checkLayout("/specs/ZooplaHomePage.spec", device.getTags());
    }

    @Test(dataProvider = "devices",priority =2,enabled=false)
    public void Zoopla_subHeading_onDevice(TestDevice device) throws IOException, Exception {
        load("/");
        getDriver().findElement(By.xpath("//button[@class='ui-button-secondary']")).click();
        Thread.sleep(3000);
        
        Actions actions = new Actions(getDriver());
        WebElement mainMenu = getDriver().findElement(By.xpath("//a[@class='mnav__link has-subnav'][contains(text(),'For sale')]"));
        actions.moveToElement(mainMenu);
        System.out.println("click on for rent");
        Thread.sleep(3000);
        WebElement subMenu = getDriver().findElement(By.xpath("//li[@id='mn-buy']//a[@class='subnav__link'][contains(text(),'property for sale')]"));
        actions.moveToElement(subMenu);
        actions.build().perform();
        
        System.out.println("click on Property for sale link");
        String abc= mainMenu.getText();
        System.out.println("Text is >> " + abc);
        Thread.sleep(3000);
        checkLayout("/specs/ZooplaForSaleSubHeading.spec", device.getTags());  
       
    }
        
    @Test(dataProvider = "devices",priority =3,enabled=false)
    public void loginPage_User_onDevice(TestDevice device) throws IOException, Exception {
    	load("/");
        getDriver().findElement(By.xpath("//button[@class='ui-button-secondary']")).click();
        Thread.sleep(3000);
        
        Actions actions = new Actions(getDriver());
        WebElement mainMenu = getDriver().findElement(By.xpath("//a[@class='mnav__link has-subnav'][contains(text(),'For sale')]"));
        actions.moveToElement(mainMenu);
        System.out.println("click on for rent");
        Thread.sleep(3000);
        WebElement subMenu = getDriver().findElement(By.xpath("//li[@id='mn-buy']//a[@class='subnav__link'][contains(text(),'property for sale')]"));
        actions.moveToElement(subMenu);
        
        List <WebElement> list = getDriver().findElements(By.xpath("//ul[@class='mnav mnav--primary list--narrow']/li"));

        System.out.println("list of links: " + list.size());
        Thread.sleep(5000);
        for(int i=0;i<list.size();i++) {
      	  
      	  String listitem = list.get(i).getText();
      	  System.out.println("Item  name: " + listitem);
        }
        
        actions.build().perform();
        
        List <WebElement> subheading = getDriver().findElements(By.xpath("//li[@id='mn-buy']//div[@class='subnav subnav--double']/ul/li"));

        System.out.println("list of links: " + subheading.size());
        Thread.sleep(5000);
        for(int i=0;i<subheading.size();i++) {
      	  
      	  String headinglist = subheading.get(i).getText();
      	  System.out.println("Item  name: " + headinglist);
        }
        
        System.out.println("click on Property for sale link");
        String abc= mainMenu.getText();
        System.out.println("Text is >> " + abc);
        
        String expected = "Overseas property for sale";
        String actual = getDriver().findElement(By.xpath("//li[@id='mn-buy']//a[@class='subnav__link'][contains(text(),'property for sale')]")).getText();
        Assert.assertEquals(expected, actual, "Verify error message.");
    }
    
    @Test(dataProvider = "devices",priority =1,enabled=true)
    public void Zoopla_Landing_Page_Search(TestDevice device) throws IOException, Exception {
    	load("/");
    	getDriver().findElement(By.xpath("//button[@class='ui-button-secondary']")).click();
        Thread.sleep(5000);
        System.out.println("cookies clicked");
        
        getDriver().findElement(By.name("q")).sendKeys("london");
        Thread.sleep(10000);
        
      List <WebElement> list = getDriver().findElements(By.xpath("//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']//li[@class='ui-menu-item']"));

      System.out.println("Country list: " + list.size());
      Thread.sleep(5000);
      for(int i=0;i<list.size();i++) {
    	  
    	  String listitem = list.get(i).getText();
    	  System.out.println("List Item : " + listitem);
    	  if(listitem.contains("London")) {
    		  list.get(i).click();
    		  break;
    	  }
    	  
      }
      
        Thread.sleep(5000);
        getDriver().findElement(By.xpath("//button[@id='search-submit']")).click();
        Thread.sleep(5000);
        String getUrl = getDriver().getCurrentUrl();
        
        System.out.println("URL>>> : " + getUrl);
        
        String exptUrl = "https://www.zoopla.co.uk/for-sale/property/london/?q=London&results_sort=newest_listings&search_source=home";
           
        Assert.assertEquals(exptUrl, getUrl);
        Thread.sleep(5000);
        
        
        ArrayList<String> obtainedList = new ArrayList<>(); 
        List<WebElement> elementList= getDriver().findElements(By.xpath("//*[@id=\"content\"]/ul/li//div[@class='listing-results-right clearfix']/a"));
        for(WebElement we:elementList){
           obtainedList.add(we.getText());
           
           System.out.println("house list: " + we.getText());
        }
        ArrayList<String> sortedList = new ArrayList<>();   
        for(String s:obtainedList){
        sortedList.add(s);
        }
        Collections.sort(sortedList);
        System.out.println("list in sorted :>>>>> " + " " + "\n" + sortedList + "\n");
        
        elementList.get(4).click();
        
        Thread.sleep(5000);
        
        String getValue = getDriver().findElement(By.xpath("//article[@class='dp-sidebar-wrapper__summary']//div[@class='ui-pricing']")).getText();
        
        System.out.println("Amount:>>>>> " + getValue);
        
       String getName = getDriver().findElement(By.xpath("//div[@class='dp-sidebar-wrapper__contact']//div[@class='ui-agent__text']")).getText();
        
        System.out.println("Name:>>>>> " + getName);
        
     String getPhone = getDriver().findElement(By.xpath("//div[@class='dp-grid-wrapper']//p[@class='ui-agent__tel ui-agent__text']//a[1]")).getText();
        
        System.out.println("Phone Number:>>>>> " + getPhone);
        
        getDriver().findElement(By.xpath("//div[@class='dp-sidebar-wrapper__contact']//div[@class='ui-agent__text']")).click();
        Thread.sleep(5000);
      String getfullName = getDriver().findElement(By.xpath("//h1[@class='bottom-half']")).getText();
        
        System.out.println("Full Name:>>>>> " + getfullName);
        
        Assert.assertEquals(getName, getfullName);
        
        }
    }
    

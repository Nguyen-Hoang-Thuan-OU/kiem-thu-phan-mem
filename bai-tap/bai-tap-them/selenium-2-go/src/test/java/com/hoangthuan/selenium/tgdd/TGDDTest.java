package com.hoangthuan.selenium.tgdd;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

// Tìm kiếm một sản phẩm (điện thoại di động),
// chọn sản phẩm đầu tiên trong danh sách kết quả
// để lấy giá bán và so sánh giữa
// giá được hiển thị ở dạng tóm tắt
// so với giá được hiển thị ở dạng chi tiết
public class TGDDTest {
    
    private static WebDriver myBrowser;
    
    // Khởi động trình duyệt và truy cập trang web
    @BeforeAll
    public static void setUpClass() {
        
        // Khai báo biến chứa đừng dẫn ChromeDriver
        String driverPath = "chromedriver.exe";
        
        // Khai báo biến môi trường cho máy ảo Java để đi tìm ChromeDriver
        System.setProperty("webdriver.chrome.driver", driverPath);
        
        // Mở trình duyệt ở chế độ ẩn danh
        ChromeOptions opt = new ChromeOptions();
        opt.addArguments("--incognito");
        
        // Khai báo đối tượng trình duyệt và trỏ đến trình duyệt vật lý
        myBrowser = new ChromeDriver(opt);
        
        // Mở rộng cửa sổ của trinh duyệt hết cỡ
        myBrowser.manage().window().maximize();
        
        // Nạp toàn bộ trang web vào trong myBrowser
        myBrowser.get("https://www.thegioididong.com/");
        
        // Tắt thông báo yêu cầu xác nhận địa chỉ
//        WebElement locationPopup = myBrowser.
//                findElement(By.xpath("//*[@id='lc_pop--sugg']/div/div[2]/a[2]"));
//        locationPopup.click();
    }
    
    // Đóng trình duyệt sau khi đã thực thi xong các Test Case
    @AfterAll
    public static void tearDownClass() {
        myBrowser.quit();
    }
    
    // Kiểm tra xem liệu giá được hiển thị ở chế độ tóm tắt
    // có giống với giá được hiển thị ở chế độ chi tiết
    @Test
    public void verifyPhonePriceGivenAPhoneReturnsTheSamePriceBothInBriefAndDetailsPage() throws InterruptedException {
        
        // Tìm kiếm một mẫu sản phẩm bất kì
        WebElement searchKeyWordBox = myBrowser.
                findElement(By.xpath("//input[@id='skw']"));
        searchKeyWordBox.sendKeys("iPhone 14");
        searchKeyWordBox.submit();
        
        // Chọn sản phầm đầu tiên trong kết quả tìm kiếm
        WebElement phoneBriefElement = myBrowser.
                findElement(By.xpath("//li[@class='item cat42'][1]"));
        
        // Lấy và in ra toàn bộ thông tin ở trang tóm tắt
//        String phoneDescription = phoneBriefElement.getText();
//        System.out.println("Phone 1: " + phoneDescription);
        
        // Đứng từ sản phẩm đầu tiên để tìm chính xác giá tiền của sản phẩm
        WebElement priceBriefElement = phoneBriefElement.
                findElement(By.className("price"));
        
        // Lấy và in ra giá tiền ở trang tóm tắt
        String priceBrief = priceBriefElement.getText();
        System.out.println("Price (brief): " + priceBrief);
        
        // Nhấn vào để xem chi tiết thông tin
        phoneBriefElement.click();
        
        // Chuyển trang và đợi các phần tử được nạp
        Thread.sleep(3000);
        
        // Tìm giá bán trong trang chi tiết sản phẩm
        WebElement priceDetailsElement = myBrowser.
                findElement(By.xpath("//p[@class='box-price-present']"));
        
        // Lấy và in ra giá tiền ở trang chi tiết
        String priceDetails = priceDetailsElement.getText();
        System.out.println("Price (details): " + priceDetails);
        
        // Xử lý loại bỏ dấu * trong chuỗi
        // nếu có đi kèm trong giá bán
        int index = priceDetails.indexOf('*');
        
        // Hàm indexOf() sẽ trả về -1 nếu không tìm thấy
        if (index >= 0)
            // Loại bỏ đi 2 kí tự cuối chuỗi
            priceDetails = priceDetails.substring(0, priceDetails.length() - 2);
        
        // So sánh kết quả mong đợi (priceBrief)
        // với kết quả thực tế (priceDetails)
        assertEquals(priceBrief, priceDetails);
    }
    
    // TGDD - v2
//    public void verifyPhonePriceGivenAPhoneReturnsTheSamePriceBothInBriefAndDetail() throws InterruptedException {
//        WebElement searchKeyword = myBrowser.findElement(By.id("skw"));
//        searchKeyword.sendKeys("iphone");
//        searchKeyword.submit();
//
//        Thread.sleep(3000);
//
//        WebElement phoneBriefE;
//        try {
//            phoneBriefE = myBrowser.findElement(By.xpath("//ul[@class='listproduct']/li[1]"));
//        } catch (Exception e) {
//            try {
//                phoneBriefE = myBrowser.findElement(By.xpath("//ul[@class='listsearch lowerProduct item2020 listproduct']/li[2]"));
//            } catch (Exception ee) {
//                phoneBriefE = myBrowser.findElement(By.xpath("//ul[@class='listsearch item2020 listproduct']/li[3]"));
//            }
//        }
//
//        WebElement phonePriceBriefE;
//        try {
//            phonePriceBriefE = phoneBriefE.findElement(By.className("price"));
//        } catch (Exception e) {
//            phonePriceBriefE = phoneBriefE.findElement(By.xpath("//p[@class='item-txt-online']"));
//        }
//
//        String phonePriceBrief = phonePriceBriefE.getText();
//        System.out.println("Price in brief: " + phonePriceBrief);
//        phonePriceBriefE.click();
//
//        Thread.sleep(3000);
//
//        WebElement phonePriceDetailsE;
//        String phonePriceDetails;
//        try {
//            phonePriceDetailsE = myBrowser.findElement(By.xpath("//div[@data-price='price02']/p[@class='box-price-present']"));
//        } catch (Exception e) {
//            try {
//                phonePriceDetailsE = myBrowser.findElement(By.xpath("//div[@class='box-price']/p[@class='box-price-present']"));
//            } catch (Exception ee) {
//                phonePriceDetailsE = myBrowser.findElement(By.xpath("//strong[@class='productstatus ']"));
//            }
//
//        }
//
//        phonePriceDetails = phonePriceDetailsE.getText();
//
//        if (phonePriceBrief.equalsIgnoreCase("Không kinh doanh") || phonePriceBrief.equalsIgnoreCase("Tin đồn")) {
//            phonePriceBrief = phonePriceBrief.toLowerCase();
//            phonePriceDetails = phonePriceDetails.toLowerCase();
//
//            if (phonePriceDetails.contains("sản phẩm")) {
//                phonePriceDetails = phonePriceDetails.substring(9, phonePriceDetails.length());
//            }
//
//        } else {
//            int index = phonePriceDetails.indexOf('*');
//
//            if (index >= 0) {
//                phonePriceDetails = phonePriceDetails.substring(0, phonePriceDetails.length() - 2);
//            }
//        }
//
//        System.out.println("Price in details: " + phonePriceDetails);
//
//        assertEquals(phonePriceBrief, phonePriceDetails);
//    }
    
}

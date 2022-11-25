package com.hoangthuan.selenium;

// Thử điều khiển trình duyệt Google Chrome,

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

// gọi trang google.com và tìm kiếm một từ khoá bất kì
public class Main {
    
    // Nơi nào gọi main() thì cũng phải tự xử lý ngoại lệ,
    // mà người gọi main() ở đây lại chính là hệ điều hành,
    // nên nếu có xảy ra thì hệ điều hành sẽ tự xử lý
    // bằng cách kết thúc tiến trình (end task)
    public static void main(String[] args) throws InterruptedException {
//        testGoogleWithAGivenKeyword();
//        testGoogleWithInIncognitoMode();
        testLoginWithValidAccountReturnsWelcomeMessage();

        // Thử nghiệm việc xử lý chuỗi: loại bỏ dấu * trong văn bản
//        String price = "290₫ *";
//        int index = price.indexOf('*');
//        System.out.println("index: " + index);
//        
//        String afterPrice = price;
//        if (index >= 0)
//            afterPrice = price.substring(0, price.length() - 2);
//        System.out.println("Final price (after removing *): "
//                + afterPrice);
    }
    
    // Automation Test Case #001
    
    // Title / Description: check search funtion of Google with a keyword
    
    // Preconditons:
    //      Data (keyword): Kiểm thử phần mềm
    
    // Steps:
    //      1. Open a certain browser, e.g. Chrome
    //      2. Type URL: https://google.com
    //      3. Type keyword: Kiểm thử phần mềm
    //      4. Hit [Enter] button
    
    // Expected results:
    //      The list of hyperlinks contain "Kiểm thử phần mềm" keyword
    
    // Hàm static để có thể được gọi trong main()
    public static void testGoogleWithAGivenKeyword() {
        
        // Vào ngay trong thư mục chứa code để đi tìm Browser WebDriver
        String driverPath = "chromedriver.exe";
        // Nếu để ở nơi khác thì phải khai báo đầy đủ đường dẫn
        //  Ví dụ: "D:\\swt\\project\\chromedriver.exe"
        // (Sử dụng hai dấu '\\'
        //  để tránh những ký hiệu đặc biệt trong lập trình,
        //  ví dụ: '\n' để xuống hàng)
        
        // Báo cho máy ảo Java biết rằng có một biến môi trường
        // (dành riêng cho máy ảo) với tên biến là "webdriver.chrome.driver"
        // trỏ đến giá trị là chromedriver.exe (chứa trong biến driverPath)
        System.setProperty("webdriver.chrome.driver", driverPath);
        //  -> Đưa đường dẫn ChromeDriver ánh xạ vào biến môi trường
        
        // Xem toàn bộ thông tin của máy ảo Java
//        System.getProperties();

        // Lúc này, trình duyệt được xem là một đối tượng (object),
        // tạo đối tượng trình duyệt và trỏ thẳng vào trình duyệt vật lý
        WebDriver myBrowser = new ChromeDriver();
        // Tạo một trình duyệt mới hoàn toàn,
        // không ảnh hưởng đến trình duyệt đang sử dụng,
        // có thể được điều khiển và đại cho trình duyệt thật
        
        // Mở rộng cửa sổ của trinh duyệt hết cỡ
        myBrowser.manage().window().maximize();
        
        // Nạp toàn bộ trang web vào trong myBrowser
        // (giống như khi cây DOM được tải về trình duyệt,
        //  nếu đã nằm trong máy tính nghĩa là đã được nạp vào RAM,
        //  sau đó chỉ cần nhờ trình duyệt lo việc hiển thị)
        //  * Duyệt web: tải trang web (và tài nguyên) về máy tính
        myBrowser.get("https://google.com");
        //  -> Cây DOM đã nằm trong đối tượng myBrowser (và trong RAM)
        
        // Lúc này, ta đã hoàn toàn có thể điều khiển trình duyệt
        // giống như những thao tác của người dùng
    }

    // Ném ra bên ngoài thông báo rằng có thể xảy ra ngoại lệ,
    // nơi nào sử dụng / gọi hàm thì phải xử lý ngoại lệ
    public static void testGoogleWithInIncognitoMode() throws InterruptedException {
        
        String driverPath = "chromedriver.exe";
        
        System.setProperty("webdriver.chrome.driver", driverPath);
        
        // Tuỳ chọn trước khi mở trình duyệt,
        // trước khi tạo mới đối tượng trình duyệt
        // (Liên quan đến hoạt động của hệ điều hành)
        ChromeOptions opt = new ChromeOptions();
        
        // Mở trong chế độ ẩn danh
        opt.addArguments("--incognito");
        
        // Chọn ngôn ngữ mặc định là tiếng anh
        opt.addArguments("--lang=en-GB");
        // Hai kí tự đầu tiên đại diện cho ngôn ngữ: English
        // Hai kí tự tiếp theo đại diện cho quốc gia: UNITED KINGDOM (GB)
        // https://www.w3schools.com/tags/ref_country_codes.asp
        
        WebDriver myBrowser = new ChromeDriver(opt);
        
        myBrowser.manage().window().maximize();
        
        myBrowser.get("https://google.com");
        
        // Đã có được một đống các phần tử (element) được trả về,
        // truy tìm chính xác ô / thẻ liên quan đến tìm kiếm
        // bằng cách sử dụng selector
        
        // Sử dụng đường dẫn tuyệt đối
//        WebElement searchBox = myBrowser.
//                findElement(By.xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"));
        
        // Sử dụng đường dẫn tương đối
        WebElement searchBox = myBrowser.
                findElement(By.xpath("//input[@name='q']"));
        
        // Nhập chuỗi cần tìm vào ô tìm kiếm thông qua hàm sendKeys()
        searchBox.sendKeys("Kiểm thử phần mềm");
        
        // Vì đây là hàm thao tác với hệ điều hành
        // để ép ứng dụng phải "đứng hình mất 3 giây",
        // có thể phát sinh vấn đề
        // liên quan đến bộ lập trình (scheduler)
        // và phát sinh ngoại lệ,
        // vì vậy, phải bắt ngoại lệ
        Thread.sleep(3000);
        // Nhưng thay vì tự mình xử lý ngoại lệ,
        // thì lại để cho nơi gọi hàm tự xử lý ngoại lệ
        
        // Vì ô nhập nằm trong form nên sẽ sử dụng hàm submit()
        searchBox.submit();
        // Tương đương với việc nhấn [Enter] vào nút [Submit]
    }
    
    
    // Automation Test Case #002
    // Title / Description: check login funtion of guru99 with a valid account
    // User ID : mngr455731
    // Password : denYrAh
    public static void testLoginWithValidAccountReturnsWelcomeMessage() throws InterruptedException {
        String driverPath = "chromedriver.exe";
        
        System.setProperty("webdriver.chrome.driver", driverPath);
        
        ChromeOptions opt = new ChromeOptions();
        
        opt.addArguments("--incognito");
        
        opt.addArguments("--lang=en-GB");
        
        WebDriver myBrowser = new ChromeDriver(opt);
        
        myBrowser.manage().window().maximize();
        
        myBrowser.get("https://demo.guru99.com/v4/");
        
        WebElement username = myBrowser.
                findElement(By.name("uid"));
        username.sendKeys("mngr455731");
        
        WebElement password = myBrowser.
                findElement(By.cssSelector("input[name='password']"));
        password.sendKeys("denYrAh");
        
        Thread.sleep(3000);
        
        WebElement loginButton = myBrowser.
                findElement(By.xpath("//input[@name='btnLogin']"));
        loginButton.submit();
        
        // Đã chuyển sang trang quản trị của Ngân hàng Guru99
        Thread.sleep(3000);
        
        WebElement welcomeMessage = myBrowser.
                findElement(By.cssSelector("tr[class='heading3'] td"));
        System.out.println("Welcome message: " + welcomeMessage.getText());
    }
    
}

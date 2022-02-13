package com.hoangthuan.mathutil.core;

// Nếu muốn sử dụng các hàm static, có 2 cách:
// Cách 1: gọi tên class.tên hàm static
//          (nhớ import package...tên class chứa hàm static)
// Cách 2: không thèm gọi tên class chấm, chỉ cần tên hàm
//          (nhớ import static package..tên class.tên hàm static
//                                              .* để lấy tất cả các hàm static)
import static com.hoangthuan.mathutil.core.MathUtil.*;
import static org.junit.Assert.*;
import org.junit.Test;

public class FactorialTest {
    
    // Viết code dùng để test code chính MathUtil
    // Tên hàm phải nói lên mục đích của việc test
    // (chia hàm ra theo mục đích test)
    
    
    // @Test: chú thích (annotation),
    // giúp biến một hàm bất kỳ trong một class bất kỳ thành hàm main
    @Test
    // Hàm được đánh giá là xanh khi tất cả các Test Case đều xanh,
    // chỉ cần có 1 cặp expected != actual
    // nghĩa là hàm xử lý không đúng hoặc ta kỳ vọng sai.
    // Ta cần xem lại code và kiểm thử lại để đảm bảo xanh hết,
    // kết luận hàm ổn cho tất cả các tình huống đã kiểm thử
    public void checkFactorialGivenCorrectArgumentReturnWell() {
        // Kỳ vọng kết quả là 120 khi gọi hàm tính 5!
        long expected = 120;
        long actual = getFactorial(5);
        assertEquals(expected, actual);
        
        // Kỳ vọng kết quả là 720 khi gọi hàm tính 6!
        assertEquals(720, getFactorial(6));
        
        // Kỳ vọng kết quả là 1 khi gọi hàm tính 0!
        assertEquals(1, getFactorial(0));
        
        // Kỳ vọng kết quả là 1 khi gọi hàm tính 1!
        assertEquals(1, getFactorial(1));
    
        // Kỳ vọng kết quả là 24 khi gọi hàm tính 4!
        assertEquals(24, getFactorial(4));
        
        // Kỳ vọng kết quả là 6 khi gọi hàm tính 3!
        assertEquals(6, getFactorial(3));
    }
    
    // Ngoại lệ không phải là 1 giá trị,
    // ngoại lệ là 1 tình huống bất thường, có khả năng xảy ra,
    // nên không thể kiểm thử theo cách thông thường (assertEquals),
    // chỉ có thể đo lường bằng cách xem nó có xảy ra hay không,
    
    //@Test(expected = IllegalArgumentException.class)
    // Biến hàm này thành public static void main() {...}
    // (đây là cú pháp/quy tắc của bộ thư viện JUnit)
    public void checkFactorialGivenWrongArgumentThrowsException() {
        
        // Số âm và số > 20 sẽ không có dữ liệu trả về
        // nên không thể so sánh (assert) được
        getFactorial(-5);
        getFactorial(21);
        getFactorial(22);
    }
    
}

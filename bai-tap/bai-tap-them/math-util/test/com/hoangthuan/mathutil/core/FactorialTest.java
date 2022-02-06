/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.hoangthuan.mathutil.core;


import static org.junit.Assert.*;
import org.junit.Test;


/**
 *
 * @author Nguyen Hoang Thuan
 */
public class FactorialTest {
    
    // Viết code dùng để test code chính MathUtil
    // Tên hàm phải nói lên mục đích của việc test
    // (chia hàm ra theo mục đích test)
    
    @Test
    // Hàm được đánh giá là xanh khi tất cả các Test Case đều xanh,
    // chỉ cần có 1 cặp expected != actual
    // nghĩa là hàm xử lý không đúng hoặc ta kỳ vọng sai.
    // Ta cần xem lại code và kiểm thử lại để đảm bảo xanh hết,
    // kết luận hàm ổn cho tất cả các tình huống đã kiểm thử
    public void checkFactorialGivenCorrectArgumentReturnWell() {
        // Kỳ vọng kết quả là 120 khi gọi hàm tính 5!
        long expected = 120;
        long actual = MathUtil.getFactorial(5);
        assertEquals(expected, actual);
        
        // Kỳ vọng kết quả là 720 khi gọi hàm tính 6!
        assertEquals(720, MathUtil.getFactorial(6));
        
        // Kỳ vọng kết quả là 1 khi gọi hàm tính 0!
        assertEquals(1, MathUtil.getFactorial(0));
        
        // Kỳ vọng kết quả là 1 khi gọi hàm tính 1!
        assertEquals(1, MathUtil.getFactorial(1));
    
        // Kỳ vọng kết quả là 24 khi gọi hàm tính 4!
        assertEquals(24, MathUtil.getFactorial(4));
        
        // Kỳ vọng kết quả là 6 khi gọi hàm tính 3!
        assertEquals(6, MathUtil.getFactorial(3));
    }
    
    //@Test(expected = IllegalArgumentException.class)
    // Biến hàm này thành public static void main() {...}
    // (đây là cú pháp/quy tắc của bộ thư viện JUnit)
    public void checkFactorialGivenWrongArgumentThrowsException() {
        
        // Số âm và số > 20 sẽ không có dữ liệu trả về
        // nên không thể so sánh (assert) được
        MathUtil.getFactorial(-5);
        MathUtil.getFactorial(21);
        MathUtil.getFactorial(22);
    }
    
}

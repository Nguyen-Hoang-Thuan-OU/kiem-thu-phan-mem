package com.hoangthuan.mathutil.core;

import static com.hoangthuan.mathutil.core.MathUtil.getFactorial;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

public class FactorialTest {
    
    // Tham số hoá - Parameterized
    
    // Hàm để chuẩn bị dữ liệu
    public static Object[][] initData() {
        return new Integer[][] {
                                {0, 1},
                                {1, 1},
                                {2, 2},
                                {3, 6},
                                {4, 24},
                                {5, 120},
                                {6, 720}
                               };
    }
    
    // Nhận bộ dữ liệu kiểm thử và tự động tiến hành kiểm thử
    @ParameterizedTest // Đã bao gồm @RunWith và @Test
    
    // Sử dụng dữ liệu được lấy từ hàm initData()
    @MethodSource("initData")
    public void checkFactorialGivenCorrectArgumentReturnsWell(int input, long expected) {

        //long actual = getFactorial(input);
        assertEquals(expected, getFactorial(input));
    }
    
    @Test
    public void checkFactorialGivenCorrectArgumentReturnsWell() {
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
}

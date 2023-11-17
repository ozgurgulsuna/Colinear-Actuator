/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f1xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */
/* Define PID coefficients */
/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define ENC1_A_Pin GPIO_PIN_0
#define ENC1_A_GPIO_Port GPIOA
#define ENC1_A_EXTI_IRQn EXTI0_IRQn
#define ENC1_B_Pin GPIO_PIN_1
#define ENC1_B_GPIO_Port GPIOA
#define ENC1_B_EXTI_IRQn EXTI1_IRQn
#define ENC2_A_Pin GPIO_PIN_2
#define ENC2_A_GPIO_Port GPIOA
#define ENC2_A_EXTI_IRQn EXTI2_IRQn
#define ENC2_B_Pin GPIO_PIN_3
#define ENC2_B_GPIO_Port GPIOA
#define ENC2_B_EXTI_IRQn EXTI3_IRQn
#define ENC3_A_Pin GPIO_PIN_4
#define ENC3_A_GPIO_Port GPIOA
#define ENC3_A_EXTI_IRQn EXTI4_IRQn
#define ENC3_B_Pin GPIO_PIN_5
#define ENC3_B_GPIO_Port GPIOA
#define ENC3_B_EXTI_IRQn EXTI9_5_IRQn
#define IN1_A_Pin GPIO_PIN_10
#define IN1_A_GPIO_Port GPIOB
#define IN1_B_Pin GPIO_PIN_11
#define IN1_B_GPIO_Port GPIOB
#define IN2_A_Pin GPIO_PIN_12
#define IN2_A_GPIO_Port GPIOB
#define IN2_B_Pin GPIO_PIN_13
#define IN2_B_GPIO_Port GPIOB
#define IN3_A_Pin GPIO_PIN_14
#define IN3_A_GPIO_Port GPIOB
#define IN3_B_Pin GPIO_PIN_15
#define IN3_B_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

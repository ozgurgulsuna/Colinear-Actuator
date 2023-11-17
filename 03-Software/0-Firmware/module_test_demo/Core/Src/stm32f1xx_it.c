/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file    stm32f1xx_it.c
  * @brief   Interrupt Service Routines.
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

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f1xx_it.h"
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN TD */

/* USER CODE END TD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
/* USER CODE BEGIN PV */
extern float delta_t;
extern int duty1;
extern int duty2;
extern int duty3;
extern int enc1_pos;
extern int enc2_pos;
extern int enc3_pos;
extern uint8_t mot1_dir;
extern uint8_t mot2_dir;
extern uint8_t mot3_dir;
extern int mot1_set_pos;
extern int mot2_set_pos;
extern int mot3_set_pos;
extern GPIO_PinState LOW;
extern GPIO_PinState HIGH;
extern float kp1;
extern float kp2;
extern float kp3;
extern float kd1;
extern float kd2;
extern float kd3;
extern float ki1;
extern float ki2;
extern float ki3;

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/* External variables --------------------------------------------------------*/
extern TIM_HandleTypeDef htim1;
extern TIM_HandleTypeDef htim4;
extern DMA_HandleTypeDef hdma_usart1_rx;
extern DMA_HandleTypeDef hdma_usart1_tx;
/* USER CODE BEGIN EV */
float pre_pos1_error=0.0;
float pre_pos2_error=0.0;
float pre_pos3_error=0.0;
float int1_error=0.0;
float int2_error=0.0;
float int3_error=0.0;
/* USER CODE END EV */

/******************************************************************************/
/*           Cortex-M3 Processor Interruption and Exception Handlers          */
/******************************************************************************/
/**
  * @brief This function handles Non maskable interrupt.
  */
void NMI_Handler(void)
{
  /* USER CODE BEGIN NonMaskableInt_IRQn 0 */

  /* USER CODE END NonMaskableInt_IRQn 0 */
  /* USER CODE BEGIN NonMaskableInt_IRQn 1 */
  while (1)
  {
  }
  /* USER CODE END NonMaskableInt_IRQn 1 */
}

/**
  * @brief This function handles Hard fault interrupt.
  */
void HardFault_Handler(void)
{
  /* USER CODE BEGIN HardFault_IRQn 0 */

  /* USER CODE END HardFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_HardFault_IRQn 0 */
    /* USER CODE END W1_HardFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Memory management fault.
  */
void MemManage_Handler(void)
{
  /* USER CODE BEGIN MemoryManagement_IRQn 0 */

  /* USER CODE END MemoryManagement_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_MemoryManagement_IRQn 0 */
    /* USER CODE END W1_MemoryManagement_IRQn 0 */
  }
}

/**
  * @brief This function handles Prefetch fault, memory access fault.
  */
void BusFault_Handler(void)
{
  /* USER CODE BEGIN BusFault_IRQn 0 */

  /* USER CODE END BusFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_BusFault_IRQn 0 */
    /* USER CODE END W1_BusFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Undefined instruction or illegal state.
  */
void UsageFault_Handler(void)
{
  /* USER CODE BEGIN UsageFault_IRQn 0 */

  /* USER CODE END UsageFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_UsageFault_IRQn 0 */
    /* USER CODE END W1_UsageFault_IRQn 0 */
  }
}

/**
  * @brief This function handles System service call via SWI instruction.
  */
void SVC_Handler(void)
{
  /* USER CODE BEGIN SVCall_IRQn 0 */

  /* USER CODE END SVCall_IRQn 0 */
  /* USER CODE BEGIN SVCall_IRQn 1 */

  /* USER CODE END SVCall_IRQn 1 */
}

/**
  * @brief This function handles Debug monitor.
  */
void DebugMon_Handler(void)
{
  /* USER CODE BEGIN DebugMonitor_IRQn 0 */

  /* USER CODE END DebugMonitor_IRQn 0 */
  /* USER CODE BEGIN DebugMonitor_IRQn 1 */

  /* USER CODE END DebugMonitor_IRQn 1 */
}

/**
  * @brief This function handles Pendable request for system service.
  */
void PendSV_Handler(void)
{
  /* USER CODE BEGIN PendSV_IRQn 0 */

  /* USER CODE END PendSV_IRQn 0 */
  /* USER CODE BEGIN PendSV_IRQn 1 */

  /* USER CODE END PendSV_IRQn 1 */
}

/**
  * @brief This function handles System tick timer.
  */
void SysTick_Handler(void)
{
  /* USER CODE BEGIN SysTick_IRQn 0 */

  /* USER CODE END SysTick_IRQn 0 */
  HAL_IncTick();
  /* USER CODE BEGIN SysTick_IRQn 1 */

  /* USER CODE END SysTick_IRQn 1 */
}

/******************************************************************************/
/* STM32F1xx Peripheral Interrupt Handlers                                    */
/* Add here the Interrupt Handlers for the used peripherals.                  */
/* For the available peripheral interrupt handler names,                      */
/* please refer to the startup file (startup_stm32f1xx.s).                    */
/******************************************************************************/

/**
  * @brief This function handles EXTI line0 interrupt.
  */
void EXTI0_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI0_IRQn 0 */
	/* Check the direction of the first motor */
	if(HAL_GPIO_ReadPin(GPIOA, ENC1_B_Pin)){
		/* Update the position of the first motor */
		enc1_pos ++;
	}else{
		enc1_pos --;

	}


  /* USER CODE END EXTI0_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC1_A_Pin);
  /* USER CODE BEGIN EXTI0_IRQn 1 */

  /* USER CODE END EXTI0_IRQn 1 */
}

/**
  * @brief This function handles EXTI line1 interrupt.
  */
void EXTI1_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI1_IRQn 0 */

  /* USER CODE END EXTI1_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC1_B_Pin);
  /* USER CODE BEGIN EXTI1_IRQn 1 */

  /* USER CODE END EXTI1_IRQn 1 */
}

/**
  * @brief This function handles EXTI line2 interrupt.
  */
void EXTI2_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI2_IRQn 0 */
	/* Check the direction of the second motor */
		if(HAL_GPIO_ReadPin(GPIOA, ENC2_B_Pin)){
			/* Update the position of the first motor */
			enc2_pos ++;
		}else{
			enc2_pos --;

		}
  /* USER CODE END EXTI2_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC2_A_Pin);
  /* USER CODE BEGIN EXTI2_IRQn 1 */

  /* USER CODE END EXTI2_IRQn 1 */
}

/**
  * @brief This function handles EXTI line3 interrupt.
  */
void EXTI3_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI3_IRQn 0 */

  /* USER CODE END EXTI3_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC2_B_Pin);
  /* USER CODE BEGIN EXTI3_IRQn 1 */

  /* USER CODE END EXTI3_IRQn 1 */
}

/**
  * @brief This function handles EXTI line4 interrupt.
  */
void EXTI4_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI4_IRQn 0 */
	/* Check the direction of the third motor */
		if(HAL_GPIO_ReadPin(GPIOA, ENC3_B_Pin)){
			/* Update the position of the first motor */
			enc3_pos ++;
		}else{
			enc3_pos --;

		}
  /* USER CODE END EXTI4_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC3_A_Pin);
  /* USER CODE BEGIN EXTI4_IRQn 1 */

  /* USER CODE END EXTI4_IRQn 1 */
}

/**
  * @brief This function handles DMA1 channel4 global interrupt.
  */
void DMA1_Channel4_IRQHandler(void)
{
  /* USER CODE BEGIN DMA1_Channel4_IRQn 0 */

  /* USER CODE END DMA1_Channel4_IRQn 0 */
  HAL_DMA_IRQHandler(&hdma_usart1_tx);
  /* USER CODE BEGIN DMA1_Channel4_IRQn 1 */

  /* USER CODE END DMA1_Channel4_IRQn 1 */
}

/**
  * @brief This function handles DMA1 channel5 global interrupt.
  */
void DMA1_Channel5_IRQHandler(void)
{
  /* USER CODE BEGIN DMA1_Channel5_IRQn 0 */

  /* USER CODE END DMA1_Channel5_IRQn 0 */
  HAL_DMA_IRQHandler(&hdma_usart1_rx);
  /* USER CODE BEGIN DMA1_Channel5_IRQn 1 */

  /* USER CODE END DMA1_Channel5_IRQn 1 */
}

/**
  * @brief This function handles EXTI line[9:5] interrupts.
  */
void EXTI9_5_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI9_5_IRQn 0 */

  /* USER CODE END EXTI9_5_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC3_B_Pin);
  /* USER CODE BEGIN EXTI9_5_IRQn 1 */

  /* USER CODE END EXTI9_5_IRQn 1 */
}

/**
  * @brief This function handles TIM1 break interrupt.
  */
void TIM1_BRK_IRQHandler(void)
{
  /* USER CODE BEGIN TIM1_BRK_IRQn 0 */
  /* USER CODE END TIM1_BRK_IRQn 0 */
  HAL_TIM_IRQHandler(&htim1);
  /* USER CODE BEGIN TIM1_BRK_IRQn 1 */

  /* USER CODE END TIM1_BRK_IRQn 1 */
}

/**
  * @brief This function handles TIM4 global interrupt.
  */
void TIM4_IRQHandler(void)
{
  /* USER CODE BEGIN TIM4_IRQn 0 */
	/* PID for motor 1*/

	/* f = 1/(delta t) = 72MHz/36000 = 2kHz */
	/* SYSCLK/ARR - Write this in a better format !!!!!!!!!!!!!!!!!!!!!!!!!!  */


	float pos1_error = mot1_set_pos - enc1_pos;
	float pos2_error = mot2_set_pos - enc2_pos;
	float pos3_error = mot3_set_pos - enc3_pos;

	float der1_error=(pos1_error-pre_pos1_error)/0.0005;
	float der2_error=(pos2_error-pre_pos2_error)/0.0005;
	float der3_error=(pos3_error-pre_pos3_error)/0.0005;

	int1_error+=pos1_error*0.0005;
	int2_error+=pos2_error*0.0005;
	int3_error+=pos3_error*0.0005;

	pre_pos1_error=pos1_error;
	pre_pos2_error=pos2_error;
	pre_pos3_error=pos3_error;

	/* Set the duty (only proportional implemented for now) */
	duty1 = (int)(kp1*pos1_error+kd1*der1_error+ki1*int1_error);
	duty2 = (int)(kp2*pos2_error+kd2*der2_error+ki2*int2_error);
	duty3 = (int)(kp3*pos3_error+kd3*der3_error+ki3*int3_error);

	/* Set the direction */
	if(duty1 > 0){
			mot1_dir = 0;
			HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, LOW);

	}
	else{
			duty1 = -duty1;
			mot1_dir = 1;
			HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, LOW);
	}
	if(duty2 > 0){
			mot2_dir = 0;
			HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, LOW);

	}
	else{
			duty2 = -duty2;
			mot2_dir = 1;
			HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, LOW);
	}
	if(duty3 > 0){
			mot3_dir = 0;
			HAL_GPIO_WritePin(GPIOB, IN3_A_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN3_B_Pin, LOW);

	}
	else{
			duty3 = -duty3;
			mot3_dir = 1;
			HAL_GPIO_WritePin(GPIOB, IN3_B_Pin, HIGH);
			HAL_GPIO_WritePin(GPIOB, IN3_A_Pin, LOW);
	}

	/* Limit the duty */
	if(duty1 > 700){
			duty1 = 700;
		}
	if(duty2 > 300){
			duty2 = 300;
		}
	if(duty3 > 700){
			duty3 = 700;
		}

	TIM1->CCR1 = duty1;
	TIM1->CCR2 = duty2;
	TIM1->CCR3 = duty3;
  /* USER CODE END TIM4_IRQn 0 */
  HAL_TIM_IRQHandler(&htim4);
  /* USER CODE BEGIN TIM4_IRQn 1 */

  /* USER CODE END TIM4_IRQn 1 */
}

/* USER CODE BEGIN 1 */

/* USER CODE END 1 */

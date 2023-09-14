import pyautogui
import time

# Define the region where you want pyautogui to operate
region_left = 460
region_top = 200
region_width = 400
region_height = 450

# Generate a list of target image filenames
target_images = ["sq{}.png".format(i) for i in range(1, 38)]
target_images.append("Finish1.png")
target_images.append("Finish2.png")
target_images.append("Finish3.png")
target_images.append("Finish4.png")
target_images.append("Finish5.png")
target_images.append("Finish6.png")
target_images.append("Finish7.png")
target_images.append("GameOver.png")
time.sleep(0.3)
while True:
    time.sleep(0.3)
    try:
        found_target = False

        for target_image in target_images:
            target_point = pyautogui.locateOnScreen(target_image, region=(region_left, region_top, region_width, region_height), grayscale=True)


            if target_point is not None:
                found_target = True

                click_x = target_point.left + target_point.width / 2
                click_y = target_point.top + target_point.height + 60
                if click_y > 660:
                    click_y = 640
                print(click_x, click_y)

                if target_image == "GameOver.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(640, 680)
                    pyautogui.click()
                    
                if target_image == "Finish1.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(710, 285)
                    pyautogui.click()
                    pyautogui.moveTo(810, 335)
                    pyautogui.click()
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(765, 300)
                    pyautogui.click()

                elif target_image == "Finish2.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(710, 285)
                    pyautogui.click()
                    pyautogui.moveTo(810, 335)
                    pyautogui.click()

                elif target_image == "Finish3.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(710, 285)
                    pyautogui.click()
                    pyautogui.moveTo(810, 335)
                    pyautogui.click()
                    pyautogui.moveTo(765, 300)
                    pyautogui.click()
                
                elif target_image == "Finish4.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(710, 285)
                    pyautogui.click()
                    pyautogui.moveTo(810, 335)
                    pyautogui.click()
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                
                elif target_image == "Finish5.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()

                elif target_image == "Finish6.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(765, 300)
                    pyautogui.click()
                    
                elif target_image == "Finish7.png":
                    print("FOUND SOLUTION")
                    pyautogui.moveTo(660, 250)
                    pyautogui.click()
                    pyautogui.moveTo(765, 300)
                    pyautogui.click()
                    
                else:
                    pyautogui.moveTo(click_x, click_y)
                    pyautogui.click()


        if not found_target:
            print("NONE FOUND")

    except KeyboardInterrupt:
        break

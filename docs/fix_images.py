import os
import glob

replacements = {
    "../figures/Poses/box.png": "../figures/pocketYogaImages/ArmLegSupport_Box_chakravakasana.png",
    "../figures/Poses/cat.png": "../figures/pocketYogaImages/ArmLegSupport_Cat_marjariasana.png",
    "../figures/Poses/cow.png": "../figures/pocketYogaImages/ArmLegSupport_Cow_bitilasana.png",
    "../figures/Poses/child.png": "../figures/pocketYogaImages/Prone_Child's_balasana.png",
    "../figures/Poses/puppy.png": "../figures/pocketYogaImages/Prone_Extended Puppy_uttana shishosana.png",
    "../figures/Poses/tiger.png": "../figures/pocketYogaImages/ArmLegSupport_Tiger_vyaghrasana.png",
    "../figures/Poses/downwardDog.png": "../figures/pocketYogaImages/ArmLegSupport_Downward-Facing Dog_adho mukha shvanasana.png",
    "../figures/Poses/chair.png": "../figures/pocketYogaImages/Standing_Chair_utkatasana.png",
    "../figures/Poses/twistedChair.png": "../figures/pocketYogaImages/Standing_Chair_utkatasana.png", # fallback since no twisted chair
    "../figures/Poses/mountain.png": "../figures/pocketYogaImages/Standing_Mountain_tadasana.png"
}

for root, _, files in os.walk("/Users/wanchang/Documents/Yoga/YogaCourseWebsite/docs"):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            for old, new in replacements.items():
                content = content.replace(old, new)
                
            if original_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Fixed {path}")


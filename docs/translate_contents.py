import os

base_dir = "/Users/wanchang/Documents/Yoga/YogaCourseWebsite/docs"

# ----------------- ENGLISH FILES -----------------
en_readme = """# Nayota Yoga 

🌐 **Language / 语言 / Sprache:** [🇨🇳 中文](#/zh/) | [🇬🇧 English](#/en/) | [🇩🇪 Deutsch](#/de/)

Welcome to the **Nayota Yoga** digital resource space. 

In the summer semester of 2026, I serendipitously became a yoga instructor, guiding a weekly 1-hour Vinyasa flow class at the Bauhaus University sports center for a total of 10 sessions. This is a very special and precious beginning for me. I want to take this opportunity to document my experiences and understanding of yoga practice, so that teaching and learning can grow together. This website serves as a repository for the theoretical content and essence of this 10-week course.

I hope to plant a seed of yoga practice in everyone, combining online theory with offline practice. The ultimate goal is to enable everyone to practice yoga regularly and quietly, guided by the feedback of their own body and mind without the need for external instruction. Step by step, you will feel the spatial changes in your body until you can observe the changes in your inner space.

<img src="en/figures/nayota-logo.png" alt="Nayota Yoga Logo" style="max-width:min(100%, 720px); height:auto;" />

## 📚 10-Week Course Structure
**Nayota Yoga 10-Week University Sports Course**

The course is centered around the practice of foundational asanas (postures). Each class will focus on experiencing one foundational pose, and through the offline Vinyasa flow, we will explore where our awareness should be directed while practicing these poses. 

1. **What is the pose?**: A standard illustration.
2. **The philosophy behind the pose**: Since a "standard" is an external average, and our bodies are non-standard, how do we adapt the pose to suit ourselves? The criterion is whether you can maintain smooth, even breathing. 
3. **Practice Tools**: Methods and regressions used to safely achieve and understand the pose.

---

> Please use the left sidebar to start your learning journey. We recommend starting with the **[Preface: Philosophy & About Me](en/preface.md)** or **[Week 1-2: Standing Poses](en/week1-standing.md)**.
"""

en_sidebar = """- [**Home**](en/README.md)
- [📖 Preface & Philosophy](en/preface.md)
  
- 🧘 Core Modules
  - [Week 1-2: Standing Poses](en/week1-standing.md)
  - [Week 3-4: Support & Flow](en/week3-support-flow.md)
  - [Week 5-6: Center & Fold](en/week5-center-fold.md)
  - [Week 7-8: Space & Backbend](en/week7-space-backbend.md)
  - [Week 9-10: Twist & Vinyasa](en/week9-twist-vinyasa.md)

- 🌐 Languages
  - [🇨🇳 Chinese Version](../zh/README.md)
  - [🇬🇧 English (Current)](#)
  - [🇩🇪 Deutsche Version](../de/README.md)
"""

en_preface = """# Preface & Philosophy

## 🎯 About Me & Nayota Yoga
I am Nayota Wuchang.
"Nayota" originates from Buddhist scriptures, meaning an immeasurable infinity. "Wuchang" (impermanence) represents the cycle of formation, existence, destruction, and emptiness—the transient nature of things. This is a pair of relative concepts: the infinite universe and the finite human life.

By choosing this name, I wish to remind myself that in the face of a finite life and infinite desires, one must have the courage to stand up, respect one's feelings, actively embrace change, adapt to the flow, and focus on the here and now. Use your finite life to maximize your true self.

In Zhuangzi's *The Secret of Caring for Life*, it is written: "My life has a limit, but knowledge has none." If we constantly strive to become a "better" version of ourselves, we can easily get lost in endless standards and external expectations. Facing our limited and fleeting selves, we should cherish and trust our own feelings, and simply try to be ourselves.

I started practicing yoga by following videos during the pandemic, eventually striving to conquer difficult, advanced poses. Now, I seek the spiritual philosophy of yoga. Yoga has strengthened my physical body and gradually helped me temper my mind.

## 🌟 My Yoga Philosophy & Five Key Elements

Throughout the 10-week course, we will integrate the following elements into every physical practice.

### 1. Breathing: Connecting Mind and Body
Breathing is something we do constantly. We can start by observing our natural rhythm.
- **Inhale**: Feel the body expanding upwards and forwards; feel the abdomen and back expanding in all directions simultaneously.
- **Exhale**: Feel the grounding downwards. As you relax and empty the deep air from your abdomen, find stability and feel the solid support of your hands or feet against the ground.

### 2. Yielding & Support
Breathe deeply into the abdomen, bringing air to every internal organ, feeling the internal space. When exhaling, empty the abdomen and feel the heart, lungs, stomach, and intestines being stably supported. Feel the support of your digestive tract. 

### 3. Expanding
From the center of your body (chest and abdomen), actively expand and lengthen upwards and downwards, or side to side. Do not just focus on extending your limbs.

### 4. Centering (Standing)
Feel the balance and stability of your organs, like a bowl of water. Avoid leaning too far forward (collapsing the lower back) or leaning backward (hunching).

### 5. Twisting
Twists also begin from the organs at the body's center. When supported, first become aware of the support from your organs, then expand it to your back, and finally to your limbs.
"""

# Skeleton files for EN
en_week1 = "# Week 1-2: Standing Poses & Yielding\n\n**Introduction**: Learn to observe our breath and connect mind and body. We don't pursue complex movements, just learn how to 'stand properly'."
en_week3 = "# Week 3-4: Support & Flow\n\n**Introduction**: When transitioning from feet to hands, how do we stabilize our shoulders and back?"
en_week5 = "# Week 5-6: Center & Fold\n\n**Introduction**: Forward folds are an inward gathering. We find our true center through folding."
en_week7 = "# Week 7-8: Space & Backbend\n\n**Introduction**: Backbends create space in the chest and abdomen. Learn to bloom elegantly with safe support."
en_week9 = "# Week 9-10: Twist & Vinyasa\n\n**Introduction**: Integrating everything. We find balance in twists and conclude with a smooth, flowing Vinyasa."

def write_f(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

os.makedirs(os.path.join(base_dir, "en"), exist_ok=True)
write_f(f"{base_dir}/en/README.md", en_readme)
write_f(f"{base_dir}/en/_sidebar.md", en_sidebar)
write_f(f"{base_dir}/en/preface.md", en_preface)
write_f(f"{base_dir}/en/week1-standing.md", en_week1)
write_f(f"{base_dir}/en/week3-support-flow.md", en_week3)
write_f(f"{base_dir}/en/week5-center-fold.md", en_week5)
write_f(f"{base_dir}/en/week7-space-backbend.md", en_week7)
write_f(f"{base_dir}/en/week9-twist-vinyasa.md", en_week9)


# ----------------- GERMAN FILES -----------------
de_readme = """# Nayota Yoga 

🌐 **Language / 语言 / Sprache:** [🇨🇳 中文](#/zh/) | [🇬🇧 English](#/en/) | [🇩🇪 Deutsch](#/de/)

Willkommen im digitalen Raum von **Nayota Yoga**.

Im Sommersemester 2026 wurde ich durch einen glücklichen Zufall Yogalehrerin und leitete wöchentlich einen einstündigen Vinyasa Flow Kurs im Sportzentrum der Bauhaus-Universität, insgesamt 10 Einheiten. Diese Website dient als Aufbewahrungsort für die theoretischen Inhalte und die Essenz dieses 10-wöchigen Kurses.

Das Ziel ist es, dass jeder nach diesem Kurs regelmäßig und in Ruhe Yoga üben kann, geleitet vom Feedback des eigenen Körpers und Geistes, ohne die Notwendigkeit einer externen Anleitung.

<img src="de/figures/nayota-logo.png" alt="Nayota Yoga Logo" style="max-width:min(100%, 720px); height:auto;" />

## 📚 10-Wochen-Kursstruktur
Der Kurs konzentriert sich auf die Praxis grundlegender Asanas (Körperhaltungen). Jedes Modul behandelt eine Basis-Asana.

1. **Was ist die Asana?**: Eine Standard-Illustration.
2. **Die Philosophie dahinter**: Wie passen wir die Pose an uns selbst an? Der Maßstab ist, ob man eine gleichmäßige Atmung aufrechterhalten kann.
3. **Praxis-Tools**: Methoden und Hilfsmittel, um die Asana sicher zu erreichen.

---

> Bitte nutzen Sie die linke Seitenleiste, um Ihre Lernreise zu beginnen. Wir empfehlen, mit dem **[Vorwort & Philosophie](de/preface.md)** oder **[Woche 1-2: Stehhaltungen (Standing Poses)](de/week1-standing.md)** zu starten.
"""

de_sidebar = """- [**Startseite**](de/README.md)
- [📖 Vorwort & Philosophie](de/preface.md)
  
- 🧘 Kernmodule
  - [Woche 1-2: Stehhaltungen & Basis](de/week1-standing.md)
  - [Woche 3-4: Stütze & Flow](de/week3-support-flow.md)
  - [Woche 5-6: Vorbeuge & Zentrum](de/week5-center-fold.md)
  - [Woche 7-8: Rückbeuge & Raum](de/week7-space-backbend.md)
  - [Woche 9-10: Drehung & Vinyasa](de/week9-twist-vinyasa.md)

- 🌐 Sprachen
  - [🇨🇳 Chinesische Version](../zh/README.md)
  - [🇬🇧 Englische Version](../en/README.md)
  - [🇩🇪 Deutsch (Aktuell)](#)
"""

de_preface = """# Vorwort & Philosophie (Preface)

## 🎯 Über mich & Nayota Yoga
Ich bin Nayota Wuchang.
"Nayota" stammt aus buddhistischen Schriften und bedeutet eine unermessliche Unendlichkeit. "Wuchang" (Vergänglichkeit) steht für den Zyklus von Entstehen, Bestehen, Vergehen und Leersein.

Mit diesem Namen möchte ich mich daran erinnern angesichts eines endlichen Lebens und unendlicher Wünsche den Mut zu haben, für mich selbst einzustehen, meine eigenen Gefühle zu respektieren und Veränderungen aktiv anzunehmen. Nutze dein endliches Leben, um dich selbst zu verwirklichen.

Ich begann während der Pandemie mit Online-Videos Yoga zu praktizieren. Jetzt suche ich nach der spirituellen Philosophie des Yoga. Yoga hat meinen physischen Körper gestärkt und mir nach und nach geholfen, meinen Geist zu formen.

## 🌟 Meine Yoga-Philosophie und Fünf Schlüsselelemente

### 1. Atmung (Breathing)
Die Atmung ist etwas, das wir ständig tun.
- **Einatmen**: Fühlen Sie, wie sich der Körper nach oben und vorne ausdehnt.
- **Ausatmen**: Spüren Sie die Erdung nach unten. Finden Sie Stabilität.

### 2. Nachgeben & Stütze (Yielding & Support)
Atmen Sie tief in den Bauch ein und bringen Sie Luft zu den inneren Organen. Spüren Sie den inneren Raum. Entleeren Sie beim Ausatmen den Bauch und spüren Sie, wie Herz, Lunge, Magen und Darm stabil gestützt werden.

### 3. Ausdehnung (Expanding)
Dehnen und verlängern Sie sich aktiv von der Körpermitte (Brust und Bauch) nach oben und unten.

### 4. Zentrierung (Centering)
Spüren Sie das Gleichgewicht und die Stabilität Ihrer Organe, wie eine Schale mit Wasser. Vermeiden Sie es, sich zu weit nach vorne oder hinten zu lehnen.

### 5. Drehung (Twisting)
Drehungen beginnen ebenfalls bei den Organen in der Körpermitte.
"""

de_week1 = "# Woche 1-2: Stehhaltungen & Basis\n\n**Einführung**: Lernen Sie, Ihren Atem zu beobachten und Geist und Körper zu verbinden. Lernen Sie, wie man 'richtig steht'."
de_week3 = "# Woche 3-4: Stütze & Flow\n\n**Einführung**: Wie stabilisieren wir unsere Schultern, wenn das Gewicht auf die Hände verlagert wird?"
de_week5 = "# Woche 5-6: Vorbeuge & Zentrum\n\n**Einführung**: Vorbeugen sind eine innere Sammlung. Wir finden unsere wahre Mitte."
de_week7 = "# Woche 7-8: Rückbeuge & Raum\n\n**Einführung**: Rückbeugen schaffen Raum in Brust und Bauch."
de_week9 = "# Woche 9-10: Drehung & Vinyasa\n\n**Einführung**: Wir finden Balance in Drehungen und schließen mit einem fließenden Vinyasa ab."

os.makedirs(os.path.join(base_dir, "de"), exist_ok=True)
write_f(f"{base_dir}/de/README.md", de_readme)
write_f(f"{base_dir}/de/_sidebar.md", de_sidebar)
write_f(f"{base_dir}/de/preface.md", de_preface)
write_f(f"{base_dir}/de/week1-standing.md", de_week1)
write_f(f"{base_dir}/de/week3-support-flow.md", de_week3)
write_f(f"{base_dir}/de/week5-center-fold.md", de_week5)
write_f(f"{base_dir}/de/week7-space-backbend.md", de_week7)
write_f(f"{base_dir}/de/week9-twist-vinyasa.md", de_week9)

import numpy as np
import matplotlib.pyplot as plt

# --- ТВОИ ДАННЫЕ 1.2v ---
limit = 2.0  # Теперь шкала - это сам D-factor

def draw_perfect_map():
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#050505')
    
    # 1. Генерируем градиент "киселя"
    r = np.linspace(0, limit, 200)
    theta = np.linspace(0, 2*np.pi, 200)
    R_grid, T_grid = np.meshgrid(r, theta)
    X = R_grid * np.cos(T_grid)
    Y = R_grid * np.sin(T_grid)
    # Яркость растет пропорционально D
    Z = R_grid**2 

    ax.pcolormesh(X, Y, Z, cmap='magma', shading='gouraud', alpha=0.8)

    # 2. Граница Матрешки (ровно по краю D=2.0)
    wall = plt.Circle((0, 0), 1.95, color='red', fill=False, ls='--', lw=3, alpha=0.7)
    ax.add_patch(wall)

    # 3. ФУНКЦИЯ ТОЧНОЙ РАССТАНОВКИ
    def place_galaxy(name, d_val, angle_deg, color, size):
        # Позиция строго по значению D
        angle = np.radians(angle_deg)
        gx = d_val * np.cos(angle)
        gy = d_val * np.sin(angle)
        
        ax.scatter(gx, gy, color=color, s=size, edgecolors='white', zorder=5)
        ax.text(gx*1.1, gy*1.1, f"{name}\n(D={d_val})", color='white', 
                fontsize=10, fontweight='bold', ha='center')

    # Расставляем по твоей победной калибровке
    place_galaxy("Млечный Путь", 1.95, 30, 'white', 200)   # У самой стенки
    place_galaxy("Андромеда", 1.45, 150, 'orange', 300) # На подступах
    place_galaxy("NGC 2403", 0.47, 240, 'cyan', 120)    # Внутренний круг
    place_galaxy("NGC 6503", 0.22, 310, 'lime', 100)    # Почти в центре

    # Оформление
    ax.scatter(0, 0, color='white', marker='*', s=150, zorder=10) # Центр
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.axis('off')
    plt.title('ФИНАЛЬНАЯ КАРТА ПРОЕКТА МАТРЁШКА v1.2\nРаспределение натяжения по D-координате', 
              color='white', fontsize=16, pad=20)
    plt.show()

draw_perfect_map()

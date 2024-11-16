function toggleCompletion(button) {
    if (!button.classList.contains('completed') && button.getAttribute('data-clicked') === 'true') {
        return;
    }

    if (button.classList.contains('completed')) {
        button.textContent = '未完成';
        button.classList.remove('completed');
        button.removeAttribute('data-clicked'); // 移除禁用状态
    } else {
        button.textContent = '已完成';
        button.classList.add('completed');
        button.setAttribute('data-clicked', 'true'); // 设置为已点击状态
        playSound();
        launchFireworks();
    }
}

function launchFireworks() {
    // 创建烟花动画的容器
    let fireworksDiv = document.getElementById('fireworks');

    if (!fireworksDiv) {
        fireworksDiv = document.createElement('div');
        fireworksDiv.id = 'fireworks';
        document.body.appendChild(fireworksDiv);

        // 创建烟花图像
        const fireworksImage = document.createElement('img');
        fireworksImage.src = 'ff.gif';  // 使用外部 GIF 或图像
        fireworksDiv.appendChild(fireworksImage);

        // 创建显示的文字
        const fireworksText = document.createElement('p');
        fireworksText.textContent = '恭喜你完成了成就！';
        fireworksDiv.appendChild(fireworksText);
    }

    // 显示动画
    fireworksDiv.style.display = 'block';

    // 3秒后隐藏动画
    setTimeout(() => {
        hideFireworks();
    }, 3000);
}

function playSound() {
    const audio = new Audio('ff.mp3');
    audio.play();
}

// 隐藏烟花动画
function hideFireworks() {
    const fireworksDiv = document.getElementById('fireworks');
    if (fireworksDiv) {
        fireworksDiv.style.display = 'none';
    }
}


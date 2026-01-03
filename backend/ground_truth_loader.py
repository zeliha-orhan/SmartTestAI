"""
Ground Truth Loader Modülü

Bu modül, test projeleri için ground truth (gerçek hata listesi) yükler.
Ground truth, Precision/Recall hesaplamak için gereklidir.

Ground Truth Formatı:
[
    {
        "file": "app.py",
        "line": 18,
        "type": "SQL_INJECTION",
        "severity": "high",
        "description": "SQL Injection vulnerability"
    }
]

Ground Truth Dosyaları:
- ground_truth/flask_demo.json
- ground_truth/vulnerable_demo.json
"""

import json
from pathlib import Path
from typing import List, Dict, Optional

# Ground truth dosyalarının bulunduğu klasör
GROUND_TRUTH_DIR = "../ground_truth"

def load_ground_truth(project_name: str) -> Optional[List[Dict]]:
    """
    Belirtilen proje için ground truth (gerçek hata listesi) yükler
    
    Args:
        project_name: Test projesi adı (örn: "flask_demo", "vulnerable_demo")
    
    Returns:
        Ground truth listesi veya None (dosya yoksa)
    """
    ground_truth_path = Path(GROUND_TRUTH_DIR) / f"{project_name}.json"
    
    if not ground_truth_path.exists():
        return None
    
    try:
        with open(ground_truth_path, "r", encoding="utf-8") as f:
            ground_truth = json.load(f)
        
        # Ground truth formatını doğrula
        if not isinstance(ground_truth, list):
            print(f"UYARI: Ground truth dosyası liste formatında değil: {ground_truth_path}")
            return None
        
        return ground_truth
    
    except Exception as e:
        print(f"UYARI: Ground truth yüklenirken hata: {e}")
        return None

def create_flask_demo_ground_truth() -> List[Dict]:
    """
    flask_demo projesi için ground truth oluşturur
    
    Not: flask_demo temiz bir proje olduğu için ground truth boş olabilir
    veya kod incelemesi sonucu tespit edilen gerçek hatalar eklenebilir.
    
    Returns:
        Ground truth listesi
    """
    # flask_demo temiz bir proje, şu an için boş
    # Gerçek kullanımda kod incelemesi yapılarak hatalar eklenebilir
    return []

def create_vulnerable_demo_ground_truth() -> List[Dict]:
    """
    vulnerable_demo projesi için ground truth oluşturur
    
    Bu proje kasıtlı olarak güvenlik açıkları içerir.
    
    Returns:
        Ground truth listesi
    """
    return [
        {
            "file": "app.py",
            "line": 18,
            "type": "SQL_INJECTION",
            "severity": "high",
            "description": "SQL Injection vulnerability in login function"
        },
        {
            "file": "app.py",
            "line": 32,
            "type": "COMMAND_INJECTION",
            "severity": "high",
            "description": "Command Injection vulnerability in ping function"
        },
        {
            "file": "app.py",
            "line": 40,
            "type": "PATH_TRAVERSAL",
            "severity": "high",
            "description": "Path Traversal vulnerability in read_file function"
        },
        {
            "file": "app.py",
            "line": 44,
            "type": "HARDCODED_SECRET",
            "severity": "medium",
            "description": "Hardcoded secret key"
        },
        {
            "file": "app.py",
            "line": 49,
            "type": "INSECURE_DESERIALIZATION",
            "severity": "high",
            "description": "Insecure deserialization using pickle"
        },
        {
            "file": "app.py",
            "line": 60,
            "type": "XSS",
            "severity": "high",
            "description": "Cross-Site Scripting vulnerability"
        }
    ]

def save_ground_truth(project_name: str, ground_truth: List[Dict]) -> str:
    """
    Ground truth'u JSON dosyası olarak kaydeder
    
    Args:
        project_name: Proje adı
        ground_truth: Ground truth listesi
    
    Returns:
        Kaydedilen dosyanın yolu
    """
    ground_truth_path = Path(GROUND_TRUTH_DIR)
    ground_truth_path.mkdir(parents=True, exist_ok=True)
    
    file_path = ground_truth_path / f"{project_name}.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(ground_truth, f, indent=2, ensure_ascii=False)
    
    return str(file_path)


import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # Varsayılan olarak doğrulamanın başarılı olduğunu kabul ediyoruz.
            # Eğer bir sorun bulursak bunu False yapacağız.
            validation_status = True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            # Bütün sütunların şemada olup olmadığını kontrol et
            for col in all_cols:
                if col not in all_schema:
                    # Eğer şemada olmayan TEK BİR sütun bile varsa,
                    # doğrulamayı başarısız yap ve döngüden çık.
                    validation_status = False
                    break # Daha fazla kontrol etmeye gerek yok

            # Durum dosyasının yazılacağı klasörü oluştur (Hata vermemesi için)
            os.makedirs(os.path.dirname(self.config.status_file), exist_ok=True)

            # Doğrulama sonucunu dosyaya SADECE BİR KEZ yaz
            with open(self.config.status_file, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            logger.info(f"Sütunların şema ile doğrulanması tamamlandı. Sonuç: {validation_status}")

            return validation_status
        
        except Exception as e:
            # Hata oluşursa logla ve hatayı yükselt
            logger.error(f"Sütun doğrulaması sırasında bir hata oluştu: {e}")
            raise e
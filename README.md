# install pre-commit
    create - .pre-commit-config.yaml
    pip install pre-commit
    pre-commit install(устанавливаем нашу настройку)

# desk for draw
    https://drive.google.com/file/d/1s06_sEs2wcnUmzBtt7tXKW_LBjFh4Jkk/view?usp=sharing

# file for url
    https://docs.google.com/spreadsheets/d/1J1eEcKVVjWlhMkDP26PAb5baP4Opq_MPgAApUw9dK-Q/edit?usp=sharing

# trello
    https://trello.com/b/G4pjuvLQ/pythondjangoteam38

# rule for commit
    origin/fixbugs/задача или номер задачи
    origin/feature/задача или номер задачи

# running Celery
    pip install -r requirements.txt
    celery -A shope worker --loglevel=info

# Running docker
    docker compose up -d --build - сборка перед стартом контейнеров
    docker compose up -d - запуск контейнеров (-d для запуска в фоне)
    docker compose down - остановка контейнеров

# Rule for architecture
    https://app.diagrams.net/#G1s06_sEs2wcnUmzBtt7tXKW_LBjFh4Jkk

    app\
        view\
           get_cart.py
           get_product.py
        model\
           product.py
           cart.py
           category.py
        repositories
            
            class CartRepository(ICart):
                """CartItemRepository"""

                    @beartype
                    def get_active_by_user(self, _user: User) -> Optional[Cart]:
                        """Получить активную корзину пользоветеля."""
                        try:
                            return Cart.objects.get(user=_user, is_active=True)
                        except Cart.DoesNotExist:
                            return None


                    @beartype
                    def save(self, model: Cart) -> None:
                        """ Сохранить корзину."""
                        model.save()


        interface
            class ICart:
                """ICart"""
            
                @abstractmethod
                def get_active_by_user(self, _user: User) -> Optional[Cart]:
                    """Получить активную корзину пользоветеля."""
                    pass
            
                @abstractmethod
                def save(self, model: Cart) -> None:
                    """ Сохранить корзину."""
                    pass
        
        usecases
             core[optional]
                 handlers
                 requestes
             handlers
             requestes
        gateways
            core[optional]
            commands
                core[optional]
                handlers
                requestes
                        client_id
                         order_id
            quiryes
                core[optional]
                handlers
                requestes


# Load fixtures
```shell
python manage.py loaddata fixtures/*.json
```

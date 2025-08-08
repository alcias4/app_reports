from pandas import DataFrame


def cal_frecuencia(
    df: DataFrame,
    min_peso: float,
    max_peso: float,
    min_ancho: float,
    max_ancho: float,
    min_largo: float,
    max_largo: float,
    columnas: list[str],
):

    peso, ancho, largo = columnas
    peso_list = dict()
    ancho_list = dict()
    largo_list = dict()
    # Todo sobre peso
    if min_peso != 0 and max_peso != 0:

        peso_cumple = df[(df[peso] >= min_peso) & (df[peso] <= max_peso)]
        peso_liviano = df[(df[peso] < min_peso)]
        peso_pesado = df[df[peso] > max_peso]

        peso_list = {
            "Total de datos": len(df[peso]),
            # Cumplimiento general
            "Cantidad que cumple": len(peso_cumple[peso]),
            "Porcentaje que cumple (%)": (len(peso_cumple[peso]) / len(df[peso])) * 100,
            # Categorías por clase
            "Cantidad peso liviano": len(peso_liviano[peso]),
            "Porcentaje liviano (%)": (len(peso_liviano[peso]) / len(df[peso])) * 100,
            "Cantidad peso pesado": len(peso_pesado[peso]),
            "Porcentaje pesado (%)": (len(peso_pesado[peso]) / len(df[peso])) * 100,
            # Estadísticas descriptivas
            "Peso promedio": df[peso].mean(),
            "Desviación estándar": df[peso].std(),
            "Máximo peso": df[peso].max(),
            "Mínimo peso": df[peso].min(),
            "Coeficiente de variación (%)": (df[peso].std() / df[peso].mean()) * 100,
        }

    # Todo sobre elogaciones a lo ancho

    if min_ancho != 0 and max_ancho != 0:

        ancho_cumple = df[(df[ancho] >= min_ancho) & (df[ancho] <= max_ancho)]
        ancho_bajo = df[(df[ancho] < min_ancho)]
        ancho_alto = df[df[ancho] > max_ancho]

        ancho_list = {
            # 1. Total general
            "Total de datos (ancho)": df[ancho].size,
            # 2. Cumplimiento
            "Cantidad que cumple el estándar": ancho_cumple[ancho].size,
            "Porcentaje que cumple (%)": (ancho_cumple[ancho].size / df[ancho].size)
            * 100,
            # 3. Casos fuera de especificación
            "Cantidad de elonga a lo anchos por debajo del estandar": ancho_bajo[
                ancho
            ].size,
            "Porcentajee elonga a lo anchos por debajo (%)": (
                ancho_bajo[ancho].size / df[ancho].size
            )
            * 100,
            "Cantidad de elogac anchos por arriba del estandar": ancho_alto[ancho].size,
            "Porcentaje de elogac anchos por arriba del estandar (%)": (
                ancho_alto[ancho].size / df[ancho].size
            )
            * 100,
            # 4. Estadísticas descriptivas
            "Elogaci a lo Ancho promedio": df[ancho].mean(),
            "Desviación estándar": df[ancho].std(),
            "Valor máximo ancho": df[ancho].max(),
            "Valor mínimo ancho": df[ancho].min(),
            "Coeficiente de variación (%)": (df[ancho].std() / df[ancho].mean()) * 100,
        }

    # Todo sobre elogacione largo
    if min_largo != 0 and max_largo != 0:

        largo_cumple = df[(df[largo] >= min_largo) & (df[largo] <= max_largo)]
        largo_corta = df[(df[largo] < min_largo)]
        largo_alto = df[df[largo] > max_largo]

        largo_list = {
            # 1. Total general
            "Total de datos (largo)": df[largo].size,
            # 2. Cumplimiento del estándar
            "Cantidad que cumple el estándar de elogac a lo largo": largo_cumple[
                largo
            ].size,
            "Porcentaje que cumple el estándar de elogac a lo largo (%)": (
                largo_cumple[largo].size / df[largo].size
            )
            * 100,
            # 3. Casos fuera de especificación
            "Cantidad de elogac a lo largos por debajo del estandar": largo_corta[
                largo
            ].size,
            "Porcentaje de elogac a lo largos por debajo del estandar (%)": (
                largo_corta[largo].size / df[largo].size
            )
            * 100,
            "Cantidad de eloga a lo largo por arriba del estandar": largo_alto[
                largo
            ].size,
            "Porcentaje de eloga a lo largo por arriba del estandar (%)": (
                largo_alto[largo].size / df[largo].size
            )
            * 100,
            # 4. Estadísticas descriptivas
            "Elogac a lo Largo promedio": df[largo].mean(),
            "Desviación estándar": df[largo].std(),
            "Valor máximo largo": df[largo].max(),
            "Valor mínimo largo": df[largo].min(),
            "Coeficiente de variación (%)": (df[largo].std() / df[largo].mean()) * 100,
        }

    if peso_list or ancho_list or largo_list:
        return [peso_list, ancho_list, largo_list]
    else:
        return None

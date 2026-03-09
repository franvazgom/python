import exercise
import pyperclip
from copy import deepcopy
from random import randint
from collections.abc import Iterable

class TestGenerator:
    def __init__(self, namespace, names):
        self.namespace = None if (namespace is None) or (namespace.strip() == "") else namespace
        self.names = names
        self.std_outputs = []

        def mock_input(input_s=None):
            self.std_outputs.append(input_s if input_s is not None else "")
        exercise.input = mock_input
        exercise.print = lambda *args: self.std_outputs.append(" ".join(map(str, args)))
    #

    def _generate_space(self, init_args):
        r"""
        Recorre `self.namespace` instanciando las clases encontradas en el
        camino. Para dichas instancias se usan los argumentos de los 
        constructores dados en `init_args`, el cual debe ser una lista de
        tuplas, cada tupla corresponde a los argumentos de constructor de
        cada clase presente en `self.namespace`, en el mismo orden.

        Solo se deben dar argumentos de consructor para las clases, el resto
        debe ser ignorado.

        Las clases y variables/atributos se detectan automáticamente.

        Si alguno solo recibe un argumento, se puede poner el elemento 
        individual, sin necesidad de ponerlo en una tupla.
        """
        init_args = deepcopy(init_args)

        if self.namespace is None:
            space_sequence = []
        else:
            space_sequence = self.namespace.split(".")
        
        space = exercise
        for elem in space_sequence:
            elem = elem.strip()
            if elem == "":
                continue

            if inspect.isclass(getattr(space, elem)):
                # Is a class
                argv = init_args.pop(0) if len(init_args) > 0 else []
                if argv is None:
                    argv = []
                elif not isinstance(argv, Iterable):
                    argv = [argv]
                space = getattr(space, elem)(*argv)
            else:
                # Asume is an object
                space = getattr(space, elem)
        #

        return space
    #

    def generate_init_args(self):
        r"""
        Genera argumentos para los constructores de las clases encontradas
        en la cadena `self.namespace`.

        Devuelve una lista de tuplas, donde cada tupla contiene los argumentos
        a pasar a los constructores de las clases encontradas en la cadena,
        en el mismo orden.

        Solo se deben dar argumentos de consructor para las clases, el resto
        debe ser ignorado.

        Si alguno solo recibe un argumento, se puede poner el elemento 
        individual, sin necesidad de ponerlo en una tupla.
        """
        init_args = []

        return init_args
    #

    def generate_names_inputs(self):
        r"""
        Genera los parámetros a pasar a todos los nombres que se van a evaluar
        encontrados en `self.names`.

        Devuelve una lista de tuplas, donde cada tupla contiene los argumentos
        a pasar a las funciones en `self.names`, en el mismo orden.

        Si la función no retorna nada, o el nombre corresponde a un atributo,
        entones se debe poner None.

        Si alguno solo recibe un argumento, se puede poner el elemento 
        individual, sin necesidad de ponerlo en una tupla.
        """
        inputs = [(randint(0,300),)]

        return inputs
    #

    def generar_tests(self, k):
        r"""
        Genera `k` tests, donde cada test evalúa las funciones/atributos 
        definidos en `self.names`, dentro de `self.namespace`.

        Se debe implementar el método `generate_init_args` para generar
        los argumentos de los constructores de las clases encotradas en la 
        cadena `self.namespace`, y el método `self.generate_names_inputs`
        para generar los parámetros a pasar a cada función de `self.names`.
        """
        fix_repr = lambda v: f"'{v}'" if isinstance(v, str) else str(v)
        fix_results = lambda res: "".join([v if t=="except" else fix_repr(v) for v,t in res])

        tests_str = ""
        for _ in range(k):
            init_args = self.generate_init_args()
            space = self._generate_space(init_args)
            names_inputs = self.generate_names_inputs()

            tests_str += f"    {{\n"
            tests_str += f"        # Namespace: str\n"
            tests_str += f"        'namespace':{fix_repr(self.namespace)},\n"
            tests_str += f"        # Constructors arguments: list[obj]\n"
            tests_str += f"        'init_args':{fix_repr(init_args)},\n"
            tests_str += f"        # Names to execute: list[str]\n"
            tests_str += f"        'names':{fix_repr(self.names)},\n"
            tests_str += f"        # Names inputs, in the same order as names: list[str]\n"
            tests_str += f"        'names_inputs':{fix_repr(names_inputs)},\n"
            tests_str += f"        # Expected results in the same order as names: list[obj]\n"
            tests_str += f"        # If the expected result is an exception, specify the name\n"
            tests_str += f"        # the exception.\n"

            # Evaluamos los nombres para registrar los resultados.
            expected_results = []
            for name in self.names:
                name = getattr(space, name)
                if callable(name):
                    inputs = names_inputs.pop(0) if len(names_inputs) > 0 else None
                    if inputs is None:
                        inputs = []
                    
                    try:
                        expected_results.append((name(*inputs), "value"))
                    except Exception as exception:
                        expected_results.append((exception.__class__.__name__, "except"))
                        
                else:
                    expected_results.append((name, "value"))
            
            tests_str += f"        'expected_results':[{fix_results(expected_results)}],\n"
            tests_str += f"        # Standard outputs via print, input, etc: list[str]\n"
            tests_str += f"        'std_outputs':[],\n"
            tests_str += f"        # Prefix error message\n"
            tests_str += f"        'error_msg':''\n"
            tests_str += f"    }},\n"
        #

        return tests_str
    #
#

if __name__ == "__main__":
    tests = TestGenerator(None, ["residuo_2_con_7"])
    pyperclip.copy(tests.generar_tests(50))




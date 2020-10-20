main_queue_name = []
main_queue_age = []
main_queue_symptom = []

priority_queue_name = []
priority_queue_age = []
priority_queue_symptom = []

fever_queue_name = []
fever_queue_age = []
fever_queue_symptoms = []

patient_name = ''
patient_age = 0
receive_symptom = ''
patient_symptoms = []

menu_option = ''
symptoms_option = ''

fever_tag = False


def patient_evaluation():
    patient_name = input('Informe o seu nome: ')
    print('\n')
    patient_age = int(input('Informe a sua idade: '))
    print('\n')

    patient_symptoms.clear()
    fever_tag = False

    while(True):
        receive_symptom = input('Por favor informe um sintoma: ')
        patient_symptoms.append(receive_symptom)

        symptoms_option = input('Deseja finalizar? (s ou n) \n\n')

        if(symptoms_option == 's'):
            break

    for fever in patient_symptoms:
        if(fever == 'febre'):
            fever_queue_name.append(patient_name)
            fever_queue_age.append(patient_age)
            fever_queue_symptoms.append(patient_symptoms)
        else:
            break

    if(fever_tag == False):
        return

    if(patient_age >= 60):
        priority_queue_name.append(patient_name)
        priority_queue_age.append(patient_age)
        priority_queue_symptom.append(patient_symptoms)

        return

    main_queue_name.append(patient_name)
    main_queue_age.append(patient_age)
    main_queue_symptom.append(patient_symptoms)


def list_patients():
    print(main_queue_name)
    print(main_queue_age)
    print(main_queue_symptom)

    print('--------------------')

    print(priority_queue_name)
    print(priority_queue_age)
    print(priority_queue_symptom)

    print('--------------------')

    print(fever_queue_name)
    print(fever_queue_name)
    print(fever_queue_symptoms)


def call_patients():
    if(fever_queue_name):
        print('Por favor se locomover a sala de atendimento (Febre) \n\n')
        print(fever_queue_name[0], '\t')
        print(fever_queue_age[0], '\t')
        print(fever_queue_symptoms[0], '\t')

        fever_queue_name.pop(0)
        fever_queue_age.pop(0)
        fever_queue_symptoms.pop(0)

        return

    elif(priority_queue_name):
        print('Por favor se locomover a sala de atendimento (PRIORITÁRIA) \n\n')
        print(priority_queue_name[0], '\t')
        print(priority_queue_age[0], '\t')
        print(priority_queue_symptom[0], '\t')

        priority_queue_name.pop(0)
        priority_queue_age.pop(0)
        priority_queue_symptom.pop(0)

        return

    elif(main_queue_name):
        print('Por favor se locomover a sala de atendimento (Normal) \n\n')
        print(main_queue_name[0], '\t')
        print(main_queue_age[0], '\t')
        print(main_queue_symptom[0], '\t')

        main_queue_name.pop(0)
        main_queue_age.pop(0)
        main_queue_symptom.pop(0)

        return

    else:
        print('Nao há pacientes na fila')
        return


def main():
    while(True):
        print('1 - Avaliação do paciente\n')
        print('2 - Listagem dos pacientes\n')
        print('3 - Chamar o primeiro da fila\n')
        print('4 - Sair\n')
        menu_option = input('Informe a sua opção: ')
        print('\n\n')

        if(menu_option == '1'):
            patient_evaluation()

        if(menu_option == '2'):
            list_patients()

        if(menu_option == '3'):
            call_patients()

        if(menu_option == '4'):
            break


main()

from sklearn.metrics import roc_curve,precision_recall_curve,auc,accuracy_score, precision_score,recall_score,f1_score,classification_report,roc_auc_score
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict




def imprimirMetricas(X_train, X_test, y_train, y_test, model, name):
    y_pred = model.predict(X_test)
    y_hat = model.predict(X_train)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    y_prob = model.predict_proba(X_test)[:, 1] # probabilidades para a 2a classe
    y_pred = model.predict(X_test) # prediçoes discretas

    print(classification_report(y_test, y_pred))
    print(roc_auc_score(y_test, y_pred))
    print('Training set accuracy: ', accuracy_score(y_train, y_hat))
    print('Test set accuracy: ', accuracy_score(y_test, y_pred))

    curva_precisao, curva_cobertura, thresholds = precision_recall_curve(y_test, y_prob)

    # calculando a área sob a curva
    auc_precisao_cobertura = auc(curva_cobertura, curva_precisao)

    print(classification_report(y_test, y_pred))
    # imprimindo
    print(f"Acurácia de teste = {accuracy}")
    print(f"AUC = {auc_precisao_cobertura}")
    print(f"Precisão = {precision}, cobertura = {recall}")

    ''' Plotando curva '''
    plt.plot(curva_cobertura, curva_precisao)
    plt.show()



    y_scores = cross_val_predict(model, X_train, y_train, cv = 10,
                            )

    fpr, tpr, thresholds = roc_curve(y_train, y_scores)
    plt.plot(fpr, tpr, linewidth=2, label = name)
    plt.plot([0,1], [0,1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.legend(loc = 'lower right')
    plt.title('Curva ROC', fontsize = 14)
    plt.show()
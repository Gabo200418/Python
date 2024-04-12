from flask import Flask, render_template, request 
import numpy as np

app = Flask(__name__)#instancia de Flask
@app.route('/') #ruta para la página principal
def index():
    return render_template ('index.html')

@app.route('/Urp_Ucw', methods=['POST']) # Definimos una ruta para manejar el proceso de multiplicación
def Urp_Ucw():
    if request.method == 'POST':
        global b5
        b5 = str(request.form['num0'])

        Un = float(request.form['num1'])

        Us = float(request.form['num2'])

        Um = Us

        Ubase = Us*np.sqrt(2)/np.sqrt(3)
       
        k = float(request.form['num3'])

        global Urpft
        Urpft = np.round(k*Us/np.sqrt(3),2)

        k_two = float(request.form['num4'])

        global Urpff
        Urpff = np.round(k_two*Us,2)

        global Urprc                              
        if Urpft>Urpff/np.sqrt(3):
            Urprc = Urpft
        else:
            Urprc = Urpff/np.sqrt(3)
        
        Urprc = np.round(Urprc, 2)

        Ue2_er = float(request.form['num5'])  

        Uet_pu_er = 1.25 * Ue2_er - 0.25

        Uet_er = Uet_pu_er*Ubase

        Up2_er = float(request.form['num6'])
        
        Upt_pu_er = 1.25 * Up2_er - 0.43

        Upt_er = np.round(Upt_pu_er*Ubase,2)

        Ue2 = float(request.form['num7'])

        Uet_pu = 1.25 * Ue2 - 0.25

        Uet = np.round(Uet_pu*Ubase,2)

        Up2 = float(request.form['num8'])

        Upt_pu = 1.25 * Up2 - 0.43

        Upt = Upt_pu * Ubase

        NPM = float(request.form['num9'])

        NPR = float(request.form['num10'])
        
        Urp_ce = np.minimum(NPM, Uet)

        if (2 * NPM) < Upt:
            Urp_el = 2* NPM
        else:
            Urp_el = Upt
        
        Urp_ex = Upt
        
       
       
       
       
       
        ####################################
        Kc = float(request.form['num22'])
        global Ucwft
        Ucwft = max(Urpft, Urprc)#
        global Ucwff
        Ucwff = Urpff #
        Ue2_el =  np.round(Ue2_er*Us*(np.sqrt(2)/np.sqrt(3)),2)    #   
        Up2_el = np.round(Up2_er*Us*(np.sqrt(2)/np.sqrt(3)),2) #
        Ups_Ue2_ft_el = np.round(NPM/Ue2_el,2) #
        Ups_Ue2_ff_el = np.round(2*NPM/Up2_el,2) #
        Kcd_ft_el = float(request.form['num23'])
        Kcd_ff_el = float(request.form['num24'])
        global Ucw_ft
        Ucw_ft = np.round(Kcd_ft_el*Urp_ce,2) #
        global Ucw_ff
        Ucw_ff = np.round(Kcd_ff_el*Urp_el,2)#duda
        Ue2_ft = np.round(Ue2*Us*(np.sqrt(2)/np.sqrt(3)),2)   #
        ue2_ff = np.round(Up2_er*Us*(np.sqrt(2)/np.sqrt(3)),2)   #
        Ups_Ue2_ft = np.round(NPM/Ue2_ft,2) #
        Ups_Ue2_ff = np.round(2*NPM/ue2_ff,2) #
        Kcd_ft = float(request.form['num25'])#
        Kcd_ff= float(request.form['num26'])#
        global Ucw_tc_ft
        Ucw_tc_ft = np.round(Kcd_ft*Urp_ce,2)#
        global Ucw_tc_ff
        Ucw_tc_ff = np.round(Kcd_ff*Urp_ex,2)#duda
        Upi_nrp = NPR #
        A = float(request.form['num27'])
        N= float(request.form['num28'])
        # l_in = np.round(a1 + a2 + a3_in + a4, 2)#
        # l_ex = np.round(a1 + a2 + a3_ex + a4, 2)#
        a1 = float(request.form['num29'])
        a2= float(request.form['num30'])
        a3_in = float(request.form['num31'])
        a3_ex = float(request.form['num32'])
        a4 = float(request.form['num33'])
        l_in = np.round(a1 + a2 + a3_in + a4, 2)#
        l_ex = np.round(a1 + a2 + a3_ex + a4, 2)#
        Lsp= float(request.form['num34'])
        La =  float(request.form['num35'])
        Ra =  float(request.form['num36'])
        Rkm =float(request.form['num37'])
        UcW_in = np.round(Upi_nrp+(A/N)*(l_in/(Lsp+La)),2)#
        Ucw_ex = np.round(Upi_nrp+(A/N)*(l_ex/(Lsp+La)),2)#
        ###################################

        # Ks_in = float(request.form['num11'])
        # Ks_ex = float(request.form['num12'])

        # Ka_fi = np.exp(m_fi*(H/8150))
        # Ka_mft = np.exp(m_mft*(H/8150))
        # Ka_mff = np.exp(m_mff*(H/8150))
        # Ka_r = np.exp(m_r*(H/8150))

        # H =  float(request.form['num13'])

        # m_fi = float(request.form['num14'])
        # m_mft = float(request.form['num15'])
        # m_mff = float(request.form['num15'])
        # m_r = float(request.form['num17'])

        # #fata en el html____ Sobretensiones temporales
        # Urw_exft = np.round(Ucw_ft*Ks_ex*Ka_fi,2)
        # Urw_exff = np.round(Ucw_ff*Ks_ex*Ka_fi,2)
        # Urw_inft = np.round(Ucw_ft*Ks_in,2)
        # Urw_inff = np.round(Ucw_ff*Ks_in,2)


        # #Sobretensiones de frente lento--- comienza el conteo
        # Urw_1 = np.round(Ucw*Ks_ex*Ka_mft,2)
        # Urw_2 = np.round(Ka_fi*Ks_ex*Ka_mff,2)
        
        # #otros equipos
        # Urw_3 = np.round(Ucw_ft*Ks_ex*Ka_mft,2)
        # Urw_4 = np.round(Ucw_ff*Ks_ex*Ka_mff,2)
        # Urw_5 = np.round(Ucw_ft*Ks_in,2)
        # Urw_6 = np.round(Ucw_ff*Ks_in,2)

        # #Sobretensiones de frente rápido
        # Urw_4 = np.round(Ucw_ff*Ks_ex*Ka_mff,2)

    
        return render_template('index.html', r1=Um, r2=Ubase, r3=Urpft, r4=Urpff, r5=Urprc, 
                               r6=Uet_pu_er, r7=Uet_er, r8=Upt_pu_er, r9=Upt_er, r910=Uet_pu, 
                               r10=Uet, r11=Upt_pu, r12=Upt, r13=Urp_ce, r14=Urp_el, r15=Urp_ex,
                               r20=Ucwft, r23=Ucwff, r24=Ue2_el, r25=Up2_el, r27=Ups_Ue2_ft_el,
                              r29=Ups_Ue2_ff_el, r30=Ucw_ft, r31=Ucw_ff, r32=Ue2_ft, r33=ue2_ff,
                               r34=Ups_Ue2_ft, r35=Ups_Ue2_ff, r38=Ucw_tc_ft,
                                 r39=Ucw_tc_ff, r40=Upi_nrp, r43=UcW_in, r44=Ucw_ex, r45=l_in, r46=l_ex)
                            #    r16=Ka_fi, r17=Ka_mft, r18=Ka_mff, r19=Ka_r)# Renderizamos el archivo HTML resultado.html con el resultado de la multiplicación


@app.route('/Urw', methods=['POST']) 
def Urw():
    if request.method == 'POST':
        UcwT1 = float(request.form['num38'])
        UcwT2 = float(request.form['num39'])
    
        Ks_in = float(request.form['num40'])
        Ks_ex = float(request.form['num41'])

        H =  float(request.form['num42'])

        m_fi = float(request.form['num43'])
        m_mft = float(request.form['num44'])
        m_mff = float(request.form['num45'])
        m_r = float(request.form['num46'])

        # H =  float(request.form['num42'])

        Ka_fi = np.exp(m_fi*(H/8150))
        Ka_mft = np.exp(m_mft*(H/8150))
        Ka_mff = np.exp(m_mff*(H/8150))
        Ka_r = np.exp(m_r*(H/8150))

        # H =  float(request.form['num42'])

        # m_fi = float(request.form['num43'])
        # m_mft = float(request.form['num44'])
        # m_mff = float(request.form['num45'])
        # m_r = float(request.form['num46'])

        #fata en el html____ Sobretensiones temporales
        Urw_exft = np.round(Ucwft*Ks_ex*Ka_fi,2)
        Urw_exff = np.round(Ucwff*Ks_ex*Ka_fi,2)
        Urw_inft = np.round(Ucwft*Ks_in,2)
        Urw_inff = np.round(Ucwff*Ks_in,2)


        #Sobretensiones de frente lento--- comienza el conteo
        Urw_1 = np.round(Ucw_ft*Ks_ex*Ka_mft,2)
        Urw_2 = np.round(Ucw_ff*Ks_ex*Ka_mff,2)
        
        #otros equipos
        Urw_3 = Ucw_tc_ft*Ks_ex*Ka_mft
        Urw_4 = Ucw_tc_ff*Ks_ex*Ka_mff
        Urw_5 = Ucw_tc_ft*Ks_in
        Urw_6 = Ucw_tc_ff*Ks_in

        #Sobretensiones de frente rápido
        Urw_7 = UcwT2*Ks_ex*Ka_r
        Urw_8 = Urw_7
        Urw_9 = UcwT1*Ks_in
        Urw_10 = Urw_9







        #Tensiones de soportabilidad normalizadas (UW)
        Ee_ai_ex_ft= np.round(Urw_1*(0.6+(Urw_1/8500)),2)
        Ee_ai_ex_ff = np.round(Urw_2*(0.6+(Urw_2/12700)),2)

        Oe_ai_ex_ft = np.round(Urw_3*(0.6+(Urw_3/8500)),2)
        Oe_ai_ex_ff = np.round(Urw_4*(0.6+(Urw_4/12700)),2)

        # Oe_ai_in_ft = np.round(Urw_5*(0.7 if b5 == "Subestación GIS" else 0.5))
        if b5 == "GIS":
            Oe_ai_in_ft = Urw_5 * 0.7
        else:
            Oe_ai_in_ft = Urw_5 * 0.5   
        
        # Oe_ai_in_ff = np.round(Urw_6*(0.7 if b5 == "Subestación GIS" else 0.5))
        if b5 == "GIS":
            Oe_ai_in_ff = Urw_6 * 0.7
        else:
            Oe_ai_in_ff = Urw_6 * 0.5  

        Si_ai_ex_ft = np.round(Urw_1*(1.05 + (Urw_1/6000)),2)
        Si_ai_ex_ff = np.round(Urw_2*(1.05+(Urw_2/9000)),2)

        ote_ai_ex_ft = np.round(Urw_3*(1.05+(Urw_3/6000)),2)
        ote_ai_ex_ff = np.round(Urw_4*(1.05+(Urw_4/9000)),2)

        # ote_ai_in_ft = np.round()
        if b5 == "GIS":
            resultado1 = Urw_5 * 1.25
        else:
            resultado1 = Urw_5 * 1.1
        # ote_ai_in_ff = np.round()
        if b5 == "GIS":
            resultado2 = Urw_6 * 1.25
        else:
            resultado2 = Urw_6 * 1.1
    

    return render_template('index.html', r47=Ka_fi, r48=Ka_mft, r49=Ka_mff, r50=Ka_r, r51=Urw_exft, r52=Urw_exff, r53=Urw_inft, r54=Urw_inff,
                           r55=Urw_1, r56=Urw_2, r57=Urw_3, r58=Urw_4, r59=Urw_5, r60=Urw_6, r61=Urw_7, r62=Urw_8, r63=Urw_9, r64=Urw_10, r65=Ee_ai_ex_ft, r66=Ee_ai_ex_ff, r67=Oe_ai_ex_ft, r68=Oe_ai_ex_ff, r69=Oe_ai_in_ft, r70=Oe_ai_in_ff, r71=Si_ai_ex_ft, r72=Si_ai_ex_ff,
                            r73=ote_ai_ex_ft, r74=ote_ai_ex_ff, r75=resultado1, r76=resultado2)
        


if __name__ == '__main__':
    app.run(debug=True) # Ejecutamos la aplicación Flask en modo debug si se ejecuta este script directamente

# r69=Oe_ai_in_ft, r70=Oe_ai_in_ff, r75=resultado1, r76=resultado2
    #                           r65=Ee_ai_ex_ft, r66=Ee_ai_ex_ff, r67=Oe_ai_ex_ft, r68=Oe_ai_ex_ff, r71=Si_ai_ex_ft, r72=Si_ai_ex_ff, r73=ote_ai_ex_ft, r74=ote_ai_ex_ff
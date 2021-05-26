# Treino de Corrida
Carolina está treinando corrida na pista de atletismo do Centro Olímpico da UnB, enquanto que sua melhor amiga, Duda, está dando todo o apoio necessário e acompanhando o tempo de cada volta (em segundos). Nesse tempo, Duda ficou impressionada com a regularidade do treino de Carolina ao perceber que ela percorreu várias voltas consecutivas fazendo exatamente o mesmo tempo em cada uma delas.

Como Duda tem que ajudar Carolina na hidratação e com instruções de treino, ela pediu sua ajuda. Escreva um algoritmo que determina o maior número de voltas seguidas em que Carolina realiza no mesmo tempo.

* Entrada

A primeira linha da entrada contém um inteiro **_N_ (1 ≤ _N_ ≤ 10³)**, indicando o número de voltas completas percorridas por Carolina em seu treino. Em seguida, existem **_N_** linhas, cada uma apresentando um número inteiro. Formalmente, a **_i_**-ésima linha descreve um número inteiro vᵢ **(10 ≤ _vᵢ_ ≤ 10⁴)**, representando o tempo (em segundos) gasto por Carolina para percorrer a **_i_**-ésima volta.

* Saída

Imprima um número inteiro indicando a maior quantidade de voltas consecutivas que foram percorridas no mesmo tempo por Carolina.

* Observações

No primeiro exemplo de teste, a resposta é **2**, pois Carolina registra o mesmo tempo ao percorrer as voltas **2** e **3** - perceba que são consecutivas;

No segundo exemplo de teste, a resposta é **4**, pois Carolina percorre as voltas **1, 2, 3** e **4** no mesmo tempo (35 segundos gastos para percorrer cada volta);

No terceiro exemplo de teste, Carolina percorre as voltas **4, 5, 6, 7** e **8** no mesmo tempo (40 segundos cada volta). No, total, são 5 voltas consecutivas.
* For example:

|Input|Result|
|-----|------|
|5<br>15<br>20<br>20<br>13<br>12|2|
|7<br>35<br>35<br>35<br>35<br>25<br>25<br>35|4|
|11<br>30<br>30<br>30<br>40<br>40<br>40<br>40<br>40<br>30<br>30<br>30|5|
|14<br>1<br>1<br>1<br>20<br>20<br>20<br>20<br>3<br>3<br>3<br>3<br>3<br>3<br>3|7|
|63<br>175<br>842<br>95<br>28<br>955<br>124<br>329<br>761<br>804<br>191<br>391<br>277<br>58<br>844<br>356<br>779<br>525<br>106<br>203<br>574<br>304<br>641<br>466<br>925<br>183<br>214<br>62<br>187<br>758<br>645<br>616<br>991<br>192<br>549<br>188<br>593<br>16<br>336<br>483<br>564<br>763<br>889<br>231<br>843<br>247<br>504<br>692<br>785<br>954<br>481<br>922<br>313<br>917<br>187<br>969<br>270<br>767<br>820<br>697<br>551<br>216<br>658<br>996|1|
|345<br>711<br>682<br>623<br>629<br>980<br>964<br>694<br>892<br>511<br>950<br>572<br>873<br>689<br>896<br>871<br>994<br>757<br>933<br>912<br>786<br>815<br>542<br>830<br>845<br>972<br>554<br>879<br>836<br>962<br>555<br>512<br>835<br>971<br>773<br>855<br>983<br>739<br>676<br>788<br>962<br>811<br>963<br>560<br>745<br>957<br>902<br>923<br>574<br>789<br>984<br>862<br>694<br>523<br>740<br>894<br>577<br>883<br>661<br>842<br>837<br>908<br>645<br>720<br>644<br>858<br>825<br>716<br>835<br>883<br>907<br>706<br>649<br>500<br>963<br>588<br>778<br>619<br>542<br>717<br>992<br>957<br>619<br>821<br>881<br>989<br>637<br>948<br>784<br>747<br>869<br>690<br>655<br>874<br>805<br>897<br>527<br>597<br>503<br>532<br>807<br>921<br>947<br>590<br>923<br>686<br>657<br>996<br>773<br>724<br>539<br>664<br>926<br>708<br>936<br>765<br>602<br>657<br>607<br>568<br>637<br>801<br>560<br>776<br>907<br>644<br>647<br>659<br>548<br>567<br>947<br>812<br>760<br>563<br>611<br>959<br>858<br>539<br>924<br>709<br>801<br>984<br>852<br>850<br>951<br>609<br>708<br>990<br>992<br>638<br>932<br>587<br>755<br>693<br>720<br>887<br>711<br>772<br>784<br>528<br>927<br>706<br>580<br>570<br>834<br>954<br>951<br>533<br>668<br>717<br>804<br>662<br>828<br>782<br>917<br>633<br>532<br>591<br>623<br>873<br>513<br>638<br>567<br>786<br>983<br>751<br>681<br>584<br>656<br>784<br>604<br>519<br>736<br>851<br>687<br>904<br>829<br>745<br>945<br>835<br>621<br>607<br>520<br>957<br>888<br>580<br>793<br>771<br>859<br>799<br>992<br>804<br>997<br>807<br>779<br>645<br>551<br>888<br>792<br>833<br>971<br>906<br>944<br>915<br>903<br>754<br>501<br>734<br>832<br>666<br>600<br>867<br>750<br>611<br>714<br>792<br>738<br>866<br>931<br>946<br>681<br>869<br>595<br>835<br>952<br>521<br>522<br>564<br>900<br>922<br>846<br>931<br>978<br>588<br>741<br>532<br>752<br>800<br>730<br>748<br>794<br>568<br>964<br>947<br>882<br>965<br>683<br>870<br>595<br>725<br>695<br>982<br>735<br>713<br>589<br>999<br>763<br>990<br>969<br>700<br>936<br>965<br>680<br>811<br>562<br>659<br>914<br>705<br>771<br>770<br>593<br>698<br>518<br>949<br>720<br>878<br>861<br>909<br>901<br>777<br>688<br>817<br>863<br>980<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>832<br>703|41|

import pandas as pd

from pyshop import ShopSession

def build_model(shop: ShopSession):
    starttime = pd.Timestamp('2018-01-23 00:00:00')
    endtime = pd.Timestamp('2018-01-26')
    shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit="hour", timeresolution=pd.Series(index=[starttime],data=[1]))

    rsv1 = shop.model.reservoir.add_object('Reservoir1')
    rsv2 = shop.model.reservoir.add_object('Reservoir2')

    # Setting the maximum volume in Mm3 via the instance 
    rsv1.max_vol.set(39)
    rsv2.max_vol.set(97.5)

    # Setting the LRL (Lowest Regulated Level) of the reservoir in masl via the instance 
    rsv1.lrl.set(860)
    rsv2.lrl.set(650)

    # Setting the HRL (Highest Regulated Level) of the reservoir in masl by command
    shop.model.reservoir.Reservoir1.hrl.set(905)
    shop.model.reservoir.Reservoir2.hrl.set(679)

    rsv1.vol_head.set(
        pd.Series([860, 862, 864, 866, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 894, 896, 898, 902, 904, 905, 907], 
                index=[0, 0.91, 1.87, 2.88, 5.07, 6.27, 7.56, 8.91, 10.34, 11.87, 13.53, 15.27, 17.11, 19.05, 21.1, 25.65, 27.96, 30.36, 35.18, 37.68, 39, 41.66], name=0))
    rsv2.vol_head.set(
        pd.Series([650, 651.28, 652.55, 653.83, 656.38, 657.66, 658.94, 660.21, 661.49, 662.77, 664.04, 665.32, 666.6, 667.87, 669.15, 671.70, 672.98, 674.26, 676.81, 678.09, 679, 680], 
                index=[0, 2.275, 4.675, 7.2, 12.675, 15.675, 18.9, 22.275, 25.85, 29.675, 33.825, 38.175, 42.775, 47.625, 52.75, 64.125, 69.9, 75.9, 87.95, 94.2, 97.5, 104.15], name=0))

    # Setting the overflow description, the (linear) relation between spillage (in m3/s) and masl.
    rsv1.flow_descr.set(pd.Series([0, 132], index=[906, 907], name=0))
    rsv2.flow_descr.set(pd.Series([0, 132], index=[679, 680], name=0))

    # Inflow to the reservoir is an example of an attribute that can be set as a time series,using indexes that relate values to points in time
    rsv2.inflow.set(pd.Series([60], [starttime]))

    # Setting the initial start reservoir height in masl
    rsv1.start_head.set(900)
    rsv2.start_head.set(670)

    # Setting the endpoint description (water value) to 'rsv1' in NOK/MWh
    rsv1.energy_value_input.set(30)
    # Setting the endpoint description (water value) to 'rsv2' in NOK/MWh
    rsv2.energy_value_input.set(10)

    # Add a plant objects to the model and instancing them
    plant1 = shop.model.plant.add_object('Plant1')
    plant2 = shop.model.plant.add_object('Plant2')

    # Setting the outlet line / tailrace height in masl
    plant1.outlet_line.set(672)
    plant2.outlet_line.set(586)

    # Setting the main loss in the plant
    plant1.main_loss.set([0])
    plant2.main_loss.set([0])

    # Setting the penstock loss in the plant. The number of penstocks are populated equal to the number of losses defined.
    plant1.penstock_loss.set([0.001])
    plant2.penstock_loss.set([0.0001,0.0002])

    # Add a generator object to the model
    p1g1 = shop.model.generator.add_object('Plant1_Generator1')
    p1g2 = shop.model.generator.add_object('Plant1_Generator2')

    p2g1 = shop.model.generator.add_object('Plant2_Generator1')
    p2g2 = shop.model.generator.add_object('Plant2_Generator2')
    p2g3 = shop.model.generator.add_object('Plant2_Generator3')
    p2g4 = shop.model.generator.add_object('Plant2_Generator4')

    # Connecting the generator to the correct plant
    p1g1.connect_to(plant1)
    p1g2.connect_to(plant1)

    p2g1.connect_to(plant2)
    p2g2.connect_to(plant2)
    p2g3.connect_to(plant2)
    p2g4.connect_to(plant2)

    # Setting the number of penstocks
    p1g1.penstock.set(1)
    p1g2.penstock.set(p1g1.penstock.get())

    p2g1.penstock.set(1)
    p2g2.penstock.set(2)
    p2g3.penstock.set(p2g2.penstock.get())
    p2g4.penstock.set(p2g2.penstock.get())

    # Setting the minimum production in MW
    p1g1.p_min.set(60)
    p1g2.p_min.set(p1g1.p_min.get())

    p2g1.p_min.set(100)
    p2g2.p_min.set(30)
    p2g3.p_min.set(p2g2.p_min.get())
    p2g4.p_min.set(p2g2.p_min.get())

    # Setting the maximum production in MW
    p1g1.p_max.set(120)
    p1g2.p_max.set(p1g1.p_max.get())

    p2g1.p_max.set(180)
    p2g2.p_max.set(55)
    p2g3.p_max.set(p2g2.p_max.get())
    p2g4.p_max.set(p2g2.p_max.get())

    # Setting the nominal production in MW
    p1g1.p_nom.set(120)
    p1g2.p_nom.set(p1g1.p_nom.get())

    p2g1.p_nom.set(180)
    p2g2.p_nom.set(55)
    p2g3.p_nom.set(p2g2.p_nom.get())
    p2g4.p_nom.set(p2g2.p_nom.get())

    # Setting the start cost in a monetary unit (i.e. $ or NOK, the model only compares costs to each other, so you just need to be sure all costs are in the same unit)
    p1g1.startcost.set(500)
    p1g2.startcost.set(p1g1.startcost.get())

    p2g1.startcost.set(600)
    p2g2.startcost.set(200)
    p2g3.startcost.set(p2g2.startcost.get())
    p2g4.startcost.set(p2g2.startcost.get())

    # Setting generator efficiency curves, which is the releation between the efficiency factor (%) and production (MW)
    p1g1.gen_eff_curve.set(pd.Series([100, 100], index=[60, 120]))
    p1g2.gen_eff_curve.set(p1g1.gen_eff_curve.get())

    p2g1.gen_eff_curve.set(pd.Series([100, 100], index=[100, 180]))
    p2g2.gen_eff_curve.set(pd.Series([100, 100], index=[30, 60]))
    p2g3.gen_eff_curve.set(p2g2.gen_eff_curve.get())
    p2g4.gen_eff_curve.set(p2g2.gen_eff_curve.get())

    # Setting  turbine efficiency curves, which is the relation between the efficiency factor (%) and release (m3/s) for different head levels (masl)
    p1g1.turb_eff_curves.set([pd.Series([85.8733, 87.0319, 88.0879, 89.0544, 89.9446, 90.7717, 91.5488, 92.2643, 92.8213, 93.1090, 93.2170, 93.0390, 92.6570, 92.1746],
                                        index=[28.12, 30.45, 32.78, 35.11, 37.45, 39.78, 42.11, 44.44, 46.77, 49.10, 51.43, 53.76, 56.10, 58.83],
                                        name=170),
                            pd.Series([86.7321, 87.9022, 88.9688, 89.9450, 90.8441, 91.6794, 92.4643, 93.1870, 93.7495, 94.0401, 94.1492, 93.9694, 93.5836, 93.0964],
                                        index=[28.12, 30.45, 32.78, 35.11, 37.45, 39.78, 42.11, 44.44, 46.77, 49.10, 51.43, 53.76, 56.10, 58.83],
                                        name=200),
                            pd.Series([87.5908, 88.7725, 89.8497, 90.8355, 91.7435, 92.5871, 93.3798, 94.1096, 94.6777, 94.9712, 95.0813, 94.8998, 94.5101, 94.0181],
                                        index=[28.12, 30.45, 32.78, 35.11, 37.45, 39.78, 42.11, 44.44, 46.77, 49.10, 51.43, 53.76, 56.10, 58.83],
                                        name=230)])
    p1g2.turb_eff_curves.set(p1g1.turb_eff_curves.get())

    p2g1.turb_eff_curves.set([pd.Series([92.7201, 93.2583, 93.7305, 94.1368, 94.4785, 94.7525, 94.9606, 95.1028, 95.1790, 95.1892, 95.1335, 95.0118, 94.8232, 94.5191],
                                        index=[126.54, 137.03, 147.51, 158.00, 168.53, 179.01, 189.50, 199.98, 210.47, 220.95, 231.44, 241.92, 252.45, 264.74],
                                        name=60)])

    p2g2.turb_eff_curves.set([pd.Series([83.8700, 85.1937, 86.3825, 87.4362, 88.3587, 89.1419, 89.7901, 90.3033, 90.6815, 90.9248, 91.0331, 91.0063, 90.8436, 90.4817],
                                        index=[40.82, 44.20, 47.58, 50.97, 54.36, 57.75, 61.13, 64.51, 67.89, 71.27, 74.66, 78.04, 81.44, 85.40],
                                        name=60)])
    p2g3.turb_eff_curves.set(p2g2.turb_eff_curves.get())
    p2g4.turb_eff_curves.set(p2g2.turb_eff_curves.get())

    # Adding a spillway between Reservoir 1 and Reservoir 2
    s_rsv1_rsv2 = shop.model.gate.add_object('s_Reservoir1_Reservoir2')

    # Adding a bypass between Reservoir 1 and Reservoir 2
    b_rsv1_rsv2 = shop.model.gate.add_object('b_Reservoir1_Reservoir2')

    # Adding a spillway between Reservoir 1 and Reservoir 2
    s_rsv2_ocean = shop.model.gate.add_object('s_Reservoir2_Ocean')

    # Adding a bypass between Reservoir 1 and Reservoir 2
    b_rsv2_ocean = shop.model.gate.add_object('b_Reservoir2_Ocean')

    # Connecting Reservoir 1 to Plant1
    rsv1.connect_to(plant1)

    # Connecting Reservoir 1 to the bypass between Reservoir1 and Reservoir2
    rsv1.connect_to(b_rsv1_rsv2,connection_type="bypass")

    # Connecting Reservoir 1 to the spillway between Reservoir1 and Reservoir2
    rsv1.connect_to(s_rsv1_rsv2,connection_type="spill")

    # Connecting Plant1 to Reservoir2
    plant1.connect_to(rsv2)

    # Connecting the bypass between Reservoir1 and Reservoir2 to Reservoir2
    b_rsv1_rsv2.connect_to(rsv2)

    # Connecting the spillway between Reservoir1 and Reservoir2 to Reservoir2
    s_rsv1_rsv2.connect_to(rsv2)

    # Connecting Reservoir2 to Plant 2
    rsv2.connect_to(plant2)

    # Connecting Reservoir2 to the bypass between Reservoir2 and Ocean
    rsv2.connect_to(b_rsv2_ocean,connection_type="bypass")

    # Connecting Reservoir2 to the spillway between Reservoir2 and Ocean
    rsv2.connect_to(s_rsv2_ocean,connection_type="spill")

    # Adding a market named "Day_ahead"
    shop.model.market.add_object('Day_ahead')

    # Instancing the market Day_ahead to 'da'
    da = shop.model.market.Day_ahead

    # Setting a sale price to the market, which is the income value (in monetary units) per produced MW
    da.sale_price.set(pd.DataFrame([32.992,31.122,29.312,28.072,30.012,33.362,42.682,74.822,77.732,62.332,55.892,46.962,42.582,40.942,39.212,39.142,41.672,46.922,37.102,32.992,31.272,29.752,28.782,28.082,27.242,26.622,25.732,25.392,25.992,27.402,28.942,32.182,33.082,32.342,30.912,30.162,30.062,29.562,29.462,29.512,29.672,30.072,29.552,28.862,28.412,28.072,27.162,25.502,26.192,25.222,24.052,23.892,23.682,26.092,28.202,30.902,31.572,31.462,31.172,30.912,30.572,30.602,30.632,31.062,32.082,36.262,34.472,32.182,31.492,30.732,29.712,28.982], 
                                index=[starttime + pd.Timedelta(hours=i) for i in range(0,72)]))

    # Setting a buy price to the market, which is the cost to buy production in the market (in monetary units) in stead of producing it yourself per MW. This is normally used when you have a load to cover or if you have pumps
    da.buy_price.set(da.sale_price.get()+0.002)

    # Setting the amount of volume able to buy in the market in MW
    da.max_buy.set(pd.Series([9999], [starttime]))

    # Setting the amount of volume able to sell (produce) in the market in MW
    da.max_sale.set(pd.Series([9999], [starttime]))

    # Setting the load that needs to be fullfilled, either by power production or by buying from the market, depending on the above parameters
    da.load.set(pd.Series([0], [starttime]))
---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_sen_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sen_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_sen_2017
dataset_id: rdls_el-sen_wfp_integratedcontextanalysis_2017
description: 'The ICA is a process of consultations supported by mapped-out data that
  produces a strategic plan describing where different combinations of programme themes
  are appropriate to achieve goals of reducing food insecurity and climate related
  shock risk. The ICA combines multi-year food security trends with natural shock
  risk data to highlight sub-national areas where different programme strategies make
  sense. Food security trend maps shows areas where safety nets can address regular
  food insecurity, and others where shocks make recovery more important. Climate-related
  natural shock risk maps show where DRR, preparedness and early warning efforts can
  complement food-security objectives. Atop this core foundation, mapped data on subjects
  including nutrition, gender, livelihoods and resilience can enrich theme-level strategic
  planning in which all pieces work together. The full group of ICA partners discuss
  these analytical results to arrive at strategic programmatic directions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_sen_2017]'
details: null
exposure:
- asset_type:
    description: Projected population distribution for 2016 across Senegal
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Livelihood zones classified by predominant agricultural activities
      in 2015
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines multi-year food security trends (2010-2017) with natural
    shock risk data (flood 2013, drought 1981-2015, land degradation 2001-2012) and
    projected population (2016) to produce sub-national risk classifications. Livelihood
    zone mapping and malnutrition prevalence data are integrated to identify areas
    where different programme strategies are appropriate for reducing food insecurity
    and climate shock vulnerability.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_sen_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought shocks from 2010-2017
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Additional food insecure population vulnerable to major flood shocks
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/eeb8c0c8738c4e7cac60b4a03239526e/data
  format: PNG
  id: resource_a69fa7aa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Prevalence of Global Acute Malnutrition, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Senegal in 2017, showing\
    \ the areas of convergence of high levels of food insecurity recurrence and major\
    \ propensity to natural shocks (floods and droughts). The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD) and HQ GIS unit and Programme\
    \ division. Cette couche contient informations regard la classification finale\
    \ r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en Senegal\
    \ en 2017, montrant les zones de convergence de niveaux elev\xE9s de r\xE9currence\
    \ d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels (inondations\
    \ et s\xE8cheresse). L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration\
    \ entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de\
    \ Programme au quartier g\xE9n\xE9rale du PAM."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9b66287f6da440a9b5d76aa8b698e593/data
  format: null
  id: resource_1f72dde8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the most predominant livelihood\
    \ zones - by second-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Senegal in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Fewsnet, 2015. Cette couche contient informations regard\
    \ les zones de moyens d'existence pr\xE9dominant - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - identifi\xE9es pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Fewsnet, 2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/db6a1644511948af8af98967c023b269/data
  format: null
  id: resource_9d9062c3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Most Predominant Livelihood Zones, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/52100960e2be43b4a4091cdfbad6f34d/data
  format: PNG
  id: resource_033bd64b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Senegal in 2017. The analysis brings together the historical\
    \ risk of natural shocks (floods ad droughts) and the recurrence of high food\
    \ insecurity with other key contextual information to provide broad programmatic\
    \ strategies by second-level administrative area. Ce document contient les r\xE9\
    sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Senegal\
    \ en 2017. L'analyse rassemble le risque historique des chocs naturels (inondations\
    \ et s\xE8cheresse) et la r\xE9currence elev\xE9e d'ins\xE9curit\xE9 alimentaire\
    \ avec autres informations contextuelles afin de fournir grandes strat\xE9gies\
    \ programmatiques par unit\xE9 administrative de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b41844b9aa8747ad871f69eef9a5d866/data
  format: null
  id: resource_1f4ba3ba
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Programmatic Recommendations Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/f2ea35d93dfb4564b0c31ff920d8add5/data
  format: PNG
  id: resource_1b5989d1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Additional Food Insecure Population in case of a Major
    Shock, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/188cd2c092a942228cc82a9cb683392f/data
  format: PNG
  id: resource_2568ebad
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - ICA Areas & Population Density (2015)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4c19717d075844f3abee58a697baa636/data
  format: PNG
  id: resource_c319151a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c553f4c189324e338e3d58e577e9c029/data
  format: PNG
  id: resource_b83dcc6d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/704a6d76de674565af6b7dbadf9ba4b3/data
  format: PNG
  id: resource_8fa665ca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Recurrence of Food Insecurity, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c463c4ebfb6c40738cffb4641e83d1d7/data
  format: PNG
  id: resource_810c3ddb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c515bb9ed1f941659277c253665eb9e7/data
  format: PNG
  id: resource_daba14f6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Food Insecure Population for Long-Term Planning, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Senegal in 2017.\
    \ The analysis, using the Analyse Globale de la Vuln\xE9rabilit\xE9, de la S\xE9\
    curit\xE9 Alimentaire et de la Nutrition (AGVSAN), Enqu\xEAtes Nationales sur\
    \ la S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN), Enqu\xEAtes Rurale sur la\
    \ S\xE9curit\xE9 Alimentaire et la Nutrition (ERASAN), Enqu\xEAte Nationale sur\
    \ la S\xE9curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) and Sites Sentinelles\
    \ data from 2010 to 2017, determines the recurrence of food insecurity conditions\
    \ - by second-level administrative area - applying a threshold equal to 20%. Ce\
    \ document Excel contient l'analyse sur l'insecurit\xE9 alimentaire utilis\xE9\
    e aux fins de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Tchad en\
    \ 2017. L'analyse, en utilisant les Analyse Globale de la Vuln\xE9rabilit\xE9\
    , de la S\xE9curit\xE9 Alimentaire et de la Nutrition (AGVSAN), Enqu\xEAtes Nationales\
    \ sur la S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN), Enqu\xEAtes Rurale sur\
    \ la S\xE9curit\xE9 Alimentaire et la Nutrition (ERASAN), Enqu\xEAte Nationale\
    \ sur la S\xE9curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) et Sites Sentinelles\
    \ du 2010 au 2017, d\xE9termine la r\xE9currence de conditions d'insecurit\xE9\
    \ alimentaire - par unit\xE9 administrative de deuxi\xE8me niveau. Le seuil de\
    \ s\xE9curit\xE9 alimentaire (mesur\xE9 par le score de consommation alimentaire\
    \ pauvre et limite) est fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/aeebf3748479486e9cbf993bab9d72a2/data
  format: null
  id: resource_d52e685d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by second-level administrative area - observed for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Senegal in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data sources: HQ OSEP GIS Analyse des donn\xE9es NASA MODIS 2001-2012,\
    \ WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation Model. The main indicators\
    \ used for the analysis were the average ecological changes observed between 2001\
    \ and 2012 and the percentage of erosion-prone surface. Cette couche contient\
    \ les donn\xE9es necessaires pour determiner le niveau de d\xE9gradation des terres\
    \ - par unit\xE9 administrative de deuxi\xE8me niveau - observ\xE9 pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Senegal en 2017. L'analyse a \xE9\
    t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de\
    \ Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier g\xE9n\xE9\
    rale du PAM. Source des donn\xE9es: HQ OSEP GIS Analyse des donn\xE9es NASA MODIS\
    \ 2001-2012, WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation Model. Les\
    \ indicateurs principaux utilis\xE9s pour l'analyse \xE9taient les changements\
    \ moyens de couverture du sol observ\xE9s entre 2001 et 2012 et la pourcentage\
    \ de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4b301e5ab9f84d6cb1c4c2d24355ddaf/data
  format: null
  id: resource_8c15a456
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the projected population figures\
    \ - by second-level administrative area - estimated for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Senegal in 2017. Data source: WFP Senegal Country\
    \ Office, 2016. The main indicator used for the analysis was the projected population\
    \ figures for 2016. Cette couche contient informations regard le nombre de personne\
    \ projet\xE9 - par unit\xE9 administrative deuxi\xE8me niveau - utilis\xE9 par\
    \ l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Senegal en 2017. Source\
    \ des donn\xE9es: WFP Bureau du Pays, 2016. L'indicateur principale utilis\xE9\
    \ pour l'analyse \xE9tait le la population projet\xE9e en 2016 par unit\xE9 administrative\
    \ de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c935adadd16a4794a3c250bbf8ff359b/data
  format: null
  id: resource_80c11699
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Projected Population, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c4fd2118c1ac4110885db73c09a2cebb/data
  format: PNG
  id: resource_3dec9786
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock risk (floods\
    \ and droughts) estimated during the Integrated Context Analysis (ICA) performed\
    \ in Senegal in 2017. The analysis was a joint effort between the Regional Bureau\
    \ in Dakar (RBD), the HQ GIS Unit and Programme division. Data sources: UNEP/UNISDR\
    \ GAR 2013, HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE) 1981-2015. Cette\
    \ couche contient informations regard le risque des chocs naturels (inondations\
    \ et s\xE8cheresse) estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des donn\xE9es CHIRPS d'estimation des\
    \ precipitations 1981-2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/955e7d3619a74c87a26ead356d4be618/data
  format: null
  id: resource_7b935062
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Natural Shocks Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Senegal: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/321b174e0e3446769f18bd3b46636b46/data
  format: PNG
  id: resource_95f46cce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Land Degradation Extent, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Senegal in 2017. The analysis brings together the historical\
    \ risk of natural shocks (floods ad droughts) and the recurrence of high food\
    \ insecurity with other key contextual information to provide broad programmatic\
    \ strategies by second-level administrative area. Ce document contient les r\xE9\
    sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Senegal\
    \ en 2017. L'analyse rassemble le risque historique des chocs naturels (inondations\
    \ et s\xE8cheresse) et la r\xE9currence elev\xE9e d'ins\xE9curit\xE9 alimentaire\
    \ avec autres informations contextuelles afin de fournir grandes strat\xE9gies\
    \ programmatiques par unit\xE9 administrative de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2f709914ccb64ba781cf5601a219ec14/data
  format: null
  id: resource_51e67b37
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Senegal in 2017. The analysis is a joint effort between the Regional\
    \ Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data source:\
    \ HQ VAM Analysis of Chirps Rainfall Estimates (RFE), 1981-2015. The main indicator\
    \ used for the analysis was the maximum number of poor growing seasons observed\
    \ in the time window of interest. Cette couche contient informations regard le\
    \ risque de s\xE8cheresse - par unit\xE9 administrative de deuxi\xE8me niveau\
    \ - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en\
    \ Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration\
    \ entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de\
    \ Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: HQ VAM Analyse\
    \ des donn\xE9es CHIRPS d'estimation des precipitations, 1981-2015. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait le nombre maximale de saisons\
    \ qui ont connu un d\xE9ficit hydrique (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c2cab4b22ff946ba8084909620c076cb/data
  format: null
  id: resource_5f113fc7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the numbers of food insecure\
    \ people - by second-level administrative unit - estimated for the purposes of\
    \ the Integrated Context Analysis (ICA) run in Senegal in 2017. The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit\
    \ and Programme division. Data source: Analyse Globale de la Vuln\xE9rabilit\xE9\
    , de la S\xE9curit\xE9 Alimentaire et de la Nutrition (AGVSAN) 2010, Enqu\xEA\
    tes Nationales sur la S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN) 2013, Enqu\xEA\
    tes Rurale sur la S\xE9curit\xE9 Alimentaire et la Nutrition (ERASAN) 2014, Enqu\xEA\
    te Nationale sur la S\xE9curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) 2016,\
    \ Sites Sentinelles 2017. The main indicators used for the analysis were the percentage\
    \ of food insecure population for long-term planning and the additional population\
    \ figures in case of a major shock. Cette couche contient informations regard\
    \ les nombres de personnes expos\xE9es \xE0 l'ins\xE9curit\xE9 alimentaire - par\
    \ unit\xE9 administrative de deuxi\xE8me niveau - employ\xE9es pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Senegal en 2017. L'analyse a \xE9\
    t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de\
    \ Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier g\xE9n\xE9\
    rale du PAM. Source des donn\xE9es: Analyse Globale de la Vuln\xE9rabilit\xE9\
    , de la S\xE9curit\xE9 Alimentaire et de la Nutrition (AGVSAN) 2010, Enqu\xEA\
    tes Nationales sur la S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN) 2013, Enqu\xEA\
    tes Rurale sur la S\xE9curit\xE9 Alimentaire et la Nutrition (ERASAN) 2014, Enqu\xEA\
    te Nationale sur la S\xE9curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) 2016,\
    \ Sites Sentinelles 2017. Les indicateurs principaux utilis\xE9s pour l'analyse\
    \ \xE9taient la pourcentage de population expos\xE9e \xE0 l'ins\xE9curit\xE9 alimentaire\
    \ pour la planification \xE0 long-terme et le nombre de personnes suppl\xE9mentaires\
    \ en cas de choc."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7fc7c3f974c24aff92d874ec46815187/data
  format: null
  id: resource_124c412e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Estimated Numbers of Food Insecure People, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the malnutrition levels - by\
    \ first-level administrative unit - used for the purposes of the Integrated Context\
    \ Analysis (ICA) run in Senegal in 2017. The analysis was a joint effort between\
    \ the Regional Bureau in Dakar (RBD) and HQ GIS Unit and Programme division. Data\
    \ sources: Analyse Globale de la Vuln\xE9rabilit\xE9, de la S\xE9curit\xE9 Alimentaire\
    \ et de la Nutrition (AGVSAN) 2010, Enqu\xEAtes Nationales sur la S\xE9curit\xE9\
    \ Alimentaire et Nutrition (ENSAN) 2013, Standardized Monitoring and Assessment\
    \ of Relief and Transitions (SMART), 2014-2015. The main indicator used for the\
    \ analysis was the prevalence of Global Acute Malnutrition (GAM), classified according\
    \ to the thresholds suggested by the World Health Organization (WHO). Cette couche\
    \ contient informations regard les niveaux de malnutrition - par unit\xE9 administrative\
    \ de premi\xE8re niveau - observ\xE9s pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Analyse Globale de la Vuln\xE9rabilit\xE9, de la S\xE9curit\xE9\
    \ Alimentaire et de la Nutrition (AGVSAN) 2010, Enqu\xEAtes Nationales sur la\
    \ S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN) 2013, Standardized Monitoring\
    \ and Assessment of Relief and Transitions (SMART), 2014-2015. L'indicateur principale\
    \ utilis\xE9 pour l'analyse \xE9tait la pr\xE9valence de Malnutrition Aig\xFC\
    e Globale (MAG), avec un seuil d'alerte fix\xE9 \xE0 10%, selon les normes et\
    \ la gamme de valeurs class\xE9s de l'OMS 2006."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/14828251ed7c4e35a690fd2872306c32/data
  format: null
  id: resource_3a8b0ce1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Prevalence of Global Acute Malnutrition, 2010-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food security trend analysis\
    \ - by second-level administrative unit - used for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Senegal in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Analyse Globale de la Vuln\xE9rabilit\xE9, de la S\xE9\
    curit\xE9 Alimentaire et de la Nutrition (AGVSAN) 2010, Enqu\xEAtes Nationales\
    \ sur la S\xE9curit\xE9 Alimentaire et Nutrition (ENSAN) 2013, Enqu\xEAtes Rurale\
    \ sur la S\xE9curit\xE9 Alimentaire et la Nutrition (ERASAN) 2014, Enqu\xEAte\
    \ Nationale sur la S\xE9curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) 2016, Sites\
    \ Sentinelles 2017. The main indicator used for the analysis was the Food Consumption\
    \ Score (FCS), with a threshold set to 20% considering that the national averages\
    \ revolve around this number. Cette couche contient les donn\xE9es d'une analyse\
    \ de tendance de la s\xE9curit\xE9 alimentaire - par unit\xE9 administrative de\
    \ deuxi\xE8me niveau - employ\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es: Analyse Globale de la Vuln\xE9rabilit\xE9, de la S\xE9curit\xE9 Alimentaire\
    \ et de la Nutrition (AGVSAN) 2010, Enqu\xEAtes Nationales sur la S\xE9curit\xE9\
    \ Alimentaire et Nutrition (ENSAN) 2013, Enqu\xEAtes Rurale sur la S\xE9curit\xE9\
    \ Alimentaire et la Nutrition (ERASAN) 2014, Enqu\xEAte Nationale sur la S\xE9\
    curit\xE9 Alimentaire au S\xE9n\xE9gal (ENSAS) 2016, Sites Sentinelles 2017. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait le score de consommation alimentaire\
    \ avec un seuil fix\xE9 \xE0 20%, compte tenu du fait que les pr\xE9valences sont\
    \ \xE9lev\xE9es et que les moyennes nationales tournent autour de ce seuil."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1e85936e4e7a4074b0e16f3e79055b12/data
  format: null
  id: resource_6d939c8e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Recurrence of Food Insecurity, 2010-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Senegal in 2017. The analysis is the result of a joint effort between\
    \ the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme division.\
    \ Data sources: UNEP/UNISDR GAR 2013. The main indicators used for the analysis\
    \ were the percentage of department surface at flood risk and the maximum expected\
    \ frequency of flood events with a 100-year return period. Cette couche contient\
    \ informations regard le risque d'inondations - par unit\xE9 administrative de\
    \ deuxi\xE8me niveau - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Senegal en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9\
    es : UNEP/UNISDR GAR, 2013. Les indicateurs principaux utilis\xE9es pour l'analyse\
    \ \xE9taient la pourcentage de surface \xE0 risque d'inondation et l'attente maximale\
    \ attendue des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b760336360a0414bae663e8b66a1b0c1/data
  format: null
  id: resource_8643bc77
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Senegal, 2017 - Flood Risk, 2013
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-sen_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Senegal: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_mrt_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mrt_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mrt_2017
dataset_id: rdls_hel-mrt_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_mrt_2017]'
details: null
exposure:
- asset_type:
    description: Projected population distribution at sub-national level for 2016
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
    description: Livelihood zones and agricultural areas classified by predominant
      livelihood type
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend data (2011-2015) with
    historical drought risk patterns (1981-2015) and livelihood zone mapping to identify
    sub-national areas vulnerable to food insecurity from climate-related shocks.
    Projected population data and land degradation indicators are integrated to support
    strategic programme planning for reducing food insecurity and shock resilience.
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
- href: https://data.humdata.org/dataset/wfp_ica_mrt_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity impact from drought shocks on population
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
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity recurrence in agricultural livelihood zones during
      lean and harvest seasons
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: "This layer contains information about the natural shock risk (floods\
    \ and droughts) - by first-level administrative unit - estimated during the Integrated\
    \ Context Analysis (ICA) performed in Mauritania in 2017. The analysis was a joint\
    \ effort between the Regional Bureau in Dakar (RBD), the HQ GIS Unit and Programme\
    \ division. Data sources: UNEP/UNISDR GAR 2013, HQ VAM Analysis of CHIRPS Rainfall\
    \ Estimates (RFE) 1981-2015. Cette couche contient informations regard le risque\
    \ des chocs naturels (inondations et s\xE8cheresse) - par unit\xE9 administrative\
    \ de premi\xE8re niveau - estim\xE9 pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Mauritanie en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des donn\xE9es CHIRPS d'estimation\
    \ des precipitations 1981-2015."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/453304361b264b3eb88140da8694cfde/data
  format: null
  id: resource_09fd1121
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Mauritania in 2017,\
    \ showing the areas of convergence of high levels of food insecurity recurrence\
    \ and major propensity to natural shocks (floods and droughts). The analysis was\
    \ a joint effort between the Regional Bureau in Dakar (RBD) and HQ GIS unit and\
    \ Programme division. Cette couche contient informations regard la classification\
    \ finale r\xE9sultant de l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en\
    \ Mauritanie en 2017, montrant les zones de convergence de niveaux elev\xE9s de\
    \ r\xE9currence d'ins\xE9curit\xE9 alimentaire et propension aux chocs naturels\
    \ (inondations et s\xE8cheresse). L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0\
    \ la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS\
    \ et la division de Programme au quartier g\xE9n\xE9rale du PAM."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/21d5800b9de444b6861a57538eb5282b/data
  format: null
  id: resource_1606d907
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fdabd3ac3f164d89819582293ce1bbf9/data
  format: PNG
  id: resource_79841b5c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the numbers of food insecure\
    \ people - by first-level administrative unit - estimated for the purposes of\
    \ the Integrated Context Analysis (ICA) run in Mauritania in 2017. The analysis\
    \ was a joint effort between the Regional Bureau in Dakar (RBD) and the HQ GIS\
    \ Unit and Programme division. Data source: Food Security Monitoring System (FSMS),\
    \ 2011-2015. The main indicators used for the analysis are the percentage of food\
    \ insecure population for long-term planning, the most vulnerable food insecure\
    \ people and the additional population figures in case of a major shock. Cette\
    \ couche contient informations regard les nombres de personnes expos\xE9es \xE0\
    \ l'ins\xE9curit\xE9 alimentaire - par unit\xE9 administrative de premi\xE8re\
    \ niveau - employ\xE9es pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9\
    e en Mauritanie en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration\
    \ entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de\
    \ Programme au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: Food Security\
    \ Monitoring System (FSMS), 2011-2015. Les indicateurs principaux utilis\xE9s\
    \ pour l'analyse \xE9taient la pourcentage de population expos\xE9e \xE0 l'ins\xE9\
    curit\xE9 alimentaire pour la planification \xE0 long-terme, la population la\
    \ plus vulnerable et le nombre de personnes suppl\xE9mentaires en cas de choc."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0e86aa238def4d94a971dcdd8b5c5c2d/data
  format: null
  id: resource_4de701a0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Estimated Numbers of Food Insecure People, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8a3916612dd443168efe06d0739b55eb/data
  format: PNG
  id: resource_afd9dec6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Most Predominant Livelihood Zones (2013) & ICA-Coded
    Human Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/66cbff8ec6004bedb7c259c670c36adc/data
  format: PNG
  id: resource_a56dfda4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Most Predominant Livelihood Zones, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5b4d337ee2ff4128a6fb415d6ecc174b/data
  format: PNG
  id: resource_a98fa6de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Estimated Number of Additional Food Insecure People
    in case of a Major Shock, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/878fc884c536495090d3bfa7ce321c03/data
  format: PNG
  id: resource_ec952cec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7e432637c16d4fe08ee965b159976426/data
  format: PNG
  id: resource_d9e0925d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Recurrence of Food Insecurity during the lean season,
    2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/db861f2e11ec4269bde49747cf989106/data
  format: PNG
  id: resource_e1dce9f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Recurrence of Food Insecurity during the harvest season,
    2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c54eafd361574b1d9183fd44d8f2d94a/data
  format: PNG
  id: resource_1aa19a35
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/74049c7096e84b8eaa19e69755cebb04/data
  format: PNG
  id: resource_258cec8d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c6eb89ef436848ab9961021bc754092e/data
  format: PNG
  id: resource_51470dd3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Estimated Number of Food Insecure People for Long-Term
    Planning, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/198f300693ac47bfa4dd3c8d9ae3a0d7/data
  format: PNG
  id: resource_a4f36427
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Recurrence of Food Insecurity, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/58dbb917b3cb4c07a2fd339eb82efdf4/data
  format: PNG
  id: resource_06fb356f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Areas & Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the projected population figures\
    \ - by first-level administrative area - estimated for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Mauritania in 2017. Data source: WFP Mauritania\
    \ Country Office, 2016. The main indicator used for the analysis was the projected\
    \ population figures for 2016. Cette couche contient informations regard le nombre\
    \ de personne projet\xE9 - par unit\xE9 administrative premi\xE8re niveau - utilis\xE9\
    \ par l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mauritanie en 2017.\
    \ Source des donn\xE9es: WFP Bureau du Pays, 2016. L'indicateur principale utilis\xE9\
    \ pour l'analyse \xE9tait le la population projet\xE9e en 2016 par unit\xE9 administrative\
    \ de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1c2f7a74129642c0a852135760f29bbd/data
  format: null
  id: resource_b34133b7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Projected Population, 2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/cc40ada35f64461da418a1130ccbdf0c/data
  format: PNG
  id: resource_86f2904f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Areas & Prevalence of Global Acute Malnutrition,
    2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Mauritania in 2017. The analysis brings together the historical\
    \ risk of natural shocks (floods and droughts) and the recurrence of high food\
    \ insecurity with other key contextual information to provide broad programmatic\
    \ strategies by first-level administrative area. Ce document contient les r\xE9\
    sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mauritanie\
    \ en 2017. L'analyse rassemble le risque historique des chocs naturels (inondations\
    \ et s\xE8cheresse) et la r\xE9currence elev\xE9e d'ins\xE9curit\xE9 alimentaire\
    \ avec autres informations contextuelles afin de fournir grandes strat\xE9gies\
    \ programmatiques par unit\xE9 administrative de premi\xE8re niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dffa38df2451434e85c99280a00250c1/data
  format: null
  id: resource_032e2964
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Technical Paper
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Mauritania in 2017.\
    \ The analysis, using the Food Security Monitoring System (FSMS) data from 2011\
    \ to 2015, determines the recurrence of food insecurity conditions - by second-level\
    \ administrative area - applying a threshold equal to 20%. Ce document Excel contient\
    \ l'analyse sur l'insecurit\xE9 alimentaire utilis\xE9e aux fins de l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Mauritanie en 2017. L'analyse,\
    \ en utilisant Food Security Monitoring System (FSMS) donn\xE9es du 2011 au 2015,\
    \ d\xE9termine la r\xE9currence de conditions d'insecurit\xE9 alimentaire - par\
    \ unit\xE9 administrative de deuxi\xE8me niveau. Le seuil de s\xE9curit\xE9 alimentaire\
    \ (mesur\xE9 par le score de consommation alimentaire pauvre et limite) est fix\xE9\
    \ \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3cc00bed255e49339f481d1f052c5dff/data
  format: null
  id: resource_769c1c1d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Food Insecurity Recurrence Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a55917f6a07b4dbcabc71131671d97cf/data
  format: PNG
  id: resource_4fd997bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - ICA Areas & Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bb748eef53d747dc99338e7edb83d1c4/data
  format: PNG
  id: resource_e93cf39b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Flood Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the land degradation phenomenon\
    \ - by first-level administrative area - observed for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Mauritania in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data sources: HQ OSEP GIS Analysis of NASA MODIS 2001-2013, WorldClim\
    \ 1970-2000, FAO data and NASA SRTM Digital Elevation Model. The main indicators\
    \ used for the analysis were the average ecological changes observed between 2001\
    \ and 2012 and the percentage of erosion-prone surface. Cette couche contient\
    \ les donn\xE9es necessaires pour determiner le niveau de d\xE9gradation des terres\
    \ - par unit\xE9 administrative de premi\xE8re niveau - observ\xE9 pendant l'Analyse\
    \ Integr\xE9e du Contexte (AIC) execut\xE9e en Mauritanie en 2017. L'analyse a\
    \ \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional\
    \ de Dakar (RBD), l'unit\xE9 GIS et la division de Programme au quartier g\xE9\
    n\xE9rale du PAM. Source des donn\xE9es: HQ OSEP GIS Analyse des donn\xE9es NASA\
    \ MODIS 2001-2013, WorldClim 1970-2000, FAO et NASA SRTM Digital Elevation Model.\
    \ Les indicateurs principaux utilis\xE9s pour l'analyse \xE9taient les changements\
    \ moyens de couverture du sol observ\xE9s entre 2001 et 2012 et la pourcentage\
    \ de surface ayant une propension \xE0 l'\xE9rosion significative."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d9d952045e7849788de214876f232136/data
  format: null
  id: resource_3ac25738
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the most predominant livelihood\
    \ zones - by first-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Mauritania in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Fewsnet, 2013. Cette couche contient informations regard\
    \ les zones de moyens d'existence pr\xE9dominant - par unit\xE9 administrative\
    \ de premi\xE8re niveau - identifi\xE9es pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Mauritanie en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Fewsnet, 2013."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a027acbf207a4f2e915366bfe1fe9b29/data
  format: null
  id: resource_18fbc6c4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Most Predominant Livelihood Zones, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the malnutrition levels - by\
    \ first-level administrative unit - used for the purposes of the Integrated Context\
    \ Analysis (ICA) run in Mauritania i 2017. The analysis was a joint effort between\
    \ the Regional Bureau in Dakar (RBD) and HQ GIS Unit and Programme division. Data\
    \ source: Food Security Monitoring System (FSMS) & Standardized Monitoring and\
    \ Assessment of Relief and Transitions (SMART), 2011-2015. The main indicator\
    \ used for the analysis was the average prevalence of Global Acute Malnutrition\
    \ (GAM), classified according to the guidelines suggested by the World Health\
    \ Organization (WHO). Cette couche contient informations regard les niveaux de\
    \ malnutrition - par unit\xE9 administrative de premi\xE8re niveau - observ\xE9\
    s pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Niger entre 2017\
    \ et 2018. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre\
    \ le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme\
    \ au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: Food Security Monitoring\
    \ System (FSMS) & Standardized Monitoring and Assessment of Relief and Transitions\
    \ (SMART), 2011-2015. L'indicateur principale utilis\xE9 pour l'analyse \xE9tait\
    \ la pr\xE9valence moyenne de Malnutrition Aig\xFCe Globale (MAG), classifi\xE9\
    e selon les normes et la gamme de valeurs class\xE9s de l'OMS 2006."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/505bdfde874a4dd7865fdd4d929fb764/data
  format: null
  id: resource_e084f15c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Prevalence of Global Acute Malnutrition, 2011-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by first-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Mauritania in 2017. The analysis is the result of a joint effort between\
    \ the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme division.\
    \ Data sources: UNEP/UNISDR GAR 2013. The main indicators used for the analysis\
    \ were the percentage of department surface at flood risk and the maximum expected\
    \ frequency of flood events with a 100-year return period. Cette couche contient\
    \ informations regard le risque d'inondations - par unit\xE9 administrative de\
    \ premi\xE8re niveau - estim\xE9 pendant l'Analyse Integr\xE9e du Contexte (AIC)\
    \ execut\xE9e en Mauritanie en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es : UNEP/UNISDR GAR, 2013. Les indicateurs principaux utilis\xE9es\
    \ pour l'analyse \xE9taient la pourcentage de surface a risque d'inondation et\
    \ l'attente maximale attendue des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/da1f40aa26924372aac34976b4b0ad4b/data
  format: null
  id: resource_31dfa852
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Flood Risk, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by first-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Mauritania in 2017. The analysis is a joint effort between the Regional\
    \ Bureau in Dakar (RBD), the HQ GIS Unit and Programme division. Data source:\
    \ HQ VAM Analysis of NDVI data, 1981-2015. The main indicator used for the analysis\
    \ was the number of poor growing seasons observed in the time window of interest.\
    \ Cette couche contient informations regard le risque de s\xE8cheresse - par unit\xE9\
    \ administrative de premi\xE8re niveau - estim\xE9e pendant l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en Mauritanie en 2017. L'analyse a \xE9t\xE9 execut\xE9\
    e gr\xE2ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: HQ VAM Analyse des donn\xE9es NDVI, 1981-2015. L'indicateur principale\
    \ utilis\xE9 pour l'analyse \xE9tait le nombre de saisons qui ont connu un d\xE9\
    ficit hydrique (mauvaises saisons de croissance)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/83311f9973a840529c6e91d3e9d332a0/data
  format: null
  id: resource_7be63adb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Drought Risk, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food security trend analysis\
    \ - by first-level administrative unit - used for the purposes of the Integrated\
    \ Context Analysis (ICA) run in Mauritania in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Food Security Monitoring System (FSMS), 2011-2015. The\
    \ main indicator used for the analysis was the Food Consumption Score (FCS), with\
    \ a threshold - referring to poor and borderline households - set to 20%. Cette\
    \ couche contient les donn\xE9es d'une analyse de tendance de la s\xE9curit\xE9\
    \ alimentaire - par unit\xE9 administrative de premi\xE8re niveau - employ\xE9\
    e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mauritanie en\
    \ 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2ce \xE0 la collaboration entre\
    \ le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9 GIS et la division de Programme\
    \ au quartier g\xE9n\xE9rale du PAM. Source des donn\xE9es: Food Security Monitoring\
    \ System (FSMS), 2011-2015. L'indicateur principale utilis\xE9 pour l'analyse\
    \ \xE9tait le score de consommation alimentaire faible et limite, avec un seuil\
    \ fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/574aa0d3fadc4962a65308bc9ddf057f/data
  format: null
  id: resource_19cd7441
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mauritania, 2017 - Recurrence of Food Insecurity, 2011-2015
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mrt_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Mauritania: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---

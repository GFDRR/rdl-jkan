---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_mli_2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mli_2014
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_mli_2014
dataset_id: rdls_lss-mli_wfp_integratedcontextanalysis_2014
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_mli_2014]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA integrates multi-year food security trends (2005-2013) with
    natural shock risk data (drought 2008-2013, flood 2011, erosion) to identify sub-national
    areas vulnerable to food insecurity. Hazard risk layers were combined with food
    insecurity assessments to produce strategic programme recommendations for reducing
    food insecurity and climate shock vulnerability.
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
- href: https://data.humdata.org/dataset/wfp_ica_mli_2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and malnutrition impacts from drought hazards
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
    description: Food insecurity impacts from flood hazards
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
  description: "This Excel file contains the food security analysis performed for\
    \ the purposes of the Integrated Context Analysis (ICA) run in Mali in 2014. The\
    \ analysis, using Emergency Food Security Assessment (EFSA), Comprehensive Food\
    \ Security Vulnerability Analysis (CFSVA), EBSAN and Fewsnet data from 2005 to\
    \ 2013, determines the trend of food insecurity conditions - by second-level administrative\
    \ area. Ce document Excel contient l'analyse sur l'insecurit\xE9 alimentaire utilis\xE9\
    e aux fins de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mali en 2014.\
    \ L'analyse, en utilisant les Emergency Food Security Assessment (EFSA), Comprehensive\
    \ Food Security Vulnerability Analysis (CFSVA), EBSAN and Fewsnet donn\xE9es du\
    \ 2005 au 2013, d\xE9termine les niveaux d'insecurit\xE9 alimentaire - par unit\xE9\
    \ administrative de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1e46901ec1a44e5bb82c27ea3771e917/data
  format: null
  id: resource_7fb0dcd5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Food Insecurity Analysis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the drought risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Mali in 2014. Data source: HQ VAM Analysis of NDVI data, 2008-2013. The\
    \ main indicators used for the analysis were the maximum number of poor growing\
    \ seasons observed in the time window of interest and the vegetation growth rate\
    \ compared to the long-term average. Cette couche contient informations regard\
    \ le risque de s\xE8cheresse - par unit\xE9 administrative de deuxi\xE8me niveau\
    \ - estim\xE9e pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en\
    \ Mali en 2014. Source des donn\xE9es: HQ VAM Analyse des donn\xE9es NDVI, 2008-2013.\
    \ Les indicateurs principaux utilis\xE9 pour l'analyse \xE9taient le nombre maximale\
    \ de saisons qui ont connu un d\xE9ficit hydrique (mauvaises saisons de croissance)\
    \ et le niveau de croissance de la v\xE9g\xE9tation par rapport \xE0 la moyenne\
    \ \xE0 long terme"
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a2adec8c7da84fd5bf143e9455ceb25a/data
  format: null
  id: resource_0ff2e6af
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Drought Risk, 2008-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the flood risk - by second-level\
    \ administrative area - estimated during the Integrated Context Analysis (ICA)\
    \ run in Mali in 2014. Data sources: UNEP/UNISDR GAR, 2011. The main indicators\
    \ used for the analysis were the percentage of district surface at flood risk\
    \ and the maximum expected frequency of flood events with a 100-year return period.\
    \ Cette couche contient informations regard le risque d'inondations - par unit\xE9\
    \ administrative de deuxi\xE8me niveau - estim\xE9e pendant l'Analyse Integr\xE9\
    e du Contexte (AIC) execut\xE9e en Mali en 2014. Source des donn\xE9es : UNEP/UNISDR\
    \ GAR, 2011. Les indicateurs principaux utilis\xE9es pour l'analyse \xE9taient\
    \ la pourcentage de surface a risuqe d'inondation et l'attente maximale attendue\
    \ des inondations."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8b2e9fb1b2494557be4ecaf4c4ca477d/data
  format: null
  id: resource_59834959
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Flood Risk, 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Integrated Context Analysis (ICA), 2014 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5d8021d7f6ef47509d2c997f195db151/data
  format: PNG
  id: resource_98dbd8f0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Erosion Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the final categorization resulting\
    \ from the Integrated Context Analysis (ICA) performed in Mali in 2014, showing\
    \ the areas of convergence of high levels of food insecurity and malnutrition\
    \ and major propensity to natural shocks (floods, droughts and erosion). Cette\
    \ couche contient informations regard la classification finale r\xE9sultant de\
    \ l'Analyse Integr\xE9e de Contexte (AIC) execut\xE9e en Mali en 2014, montrant\
    \ les zones de convergence de niveaux elev\xE9s d'ins\xE9curit\xE9 alimentaire\
    \ et malnutrition et propension aux chocs naturels (inondations, s\xE8cheresse\
    \ et \xE9rosion)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5e2e40357d4e41238597889249d68b38/data
  format: null
  id: resource_28f09ce0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This document contains the results of the Integrated Context Analysis\
    \ (ICA) conducted in Mali in 2014. The analysis brings together the historical\
    \ risk of natural shocks (floods ad droughts) and the recurrence of high food\
    \ insecurity with other key contextual information to provide broad programmatic\
    \ strategies by second-level administrative area. Ce document contient les r\xE9\
    sultats finals de l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mali\
    \ en 2014. L'analyse rassemble le risque historique des chocs naturels (inondations\
    \ et s\xE8cheresse) et la r\xE9currence elev\xE9e d'ins\xE9curit\xE9 alimentaire\
    \ avec autres informations contextuelles afin de fournir grandes strat\xE9gies\
    \ programmatiques par unit\xE9 administrative de deuxi\xE8me niveau."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4d1bbab0ddf94770b30d6aceb1a1202f/data
  format: null
  id: resource_ac9f34a8
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the natural shock risk (floods,\
    \ droughts and erosion) estimated during the Integrated Context Analysis (ICA)\
    \ performed in Mali in 2014. Data sources: UNEP/UNISDR GAR 2011, HQ VAM Analysis\
    \ of NDVI data, 2008-2013. Cette couche contient informations regard le risque\
    \ des chocs naturels (inondations, s\xE8cheresse et \xE9rosion) estim\xE9 pendant\
    \ l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mali en 2014. Source\
    \ des donn\xE9es : UNEP/UNISDR GAR 2013, HQ VAM Analyse des donn\xE9es NDVI, 2008-2013."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c4c3c4429cfd4901997549cf00975877/data
  format: null
  id: resource_0ee18637
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Natural Shock Risk
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the food insecurity and malnutrition\
    \ trend observed during the Integrated Context Analysis (ICA) run in Mali in 2014.\
    \ Data sources: Comprehensive Food Security Vulnerability Analysis (CFSVA) 2005-2009,\
    \ EBSAN 2007-2008, Emergency Food Security Assessment (EFSA) 2011-2013, Fewsnet,\
    \ Demographic and Health Survey (DHS) 2006-2012/13, Standardized Monitoring and\
    \ Assessment of Relief and Transition (SMART) 2011-2013, MIC 2010. The main indicators\
    \ used for the analysis were, among others, the Fewsnet food security classification,\
    \ the number of food security rounds where more than 30% of the households were\
    \ found in conditions of food insecurity and the prevalence of Global Acute Malnutrition\
    \ above 10%. Cette couche contient les donn\xE9es d'une analyse de tendance de\
    \ la s\xE9curit\xE9 alimentaire et malnutrition - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - employ\xE9e pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Mali en 2014. Sources des donn\xE9es: Comprehensive Food\
    \ Security Vulnerability Analysis (CFSVA) 2005-2009, EBSAN 2007-2008, Emergency\
    \ Food Security Assessment (EFSA) 2011-2013, Fewsnet, Demographic and Health Survey\
    \ (DHS) 2006-2012/13, Standardized Monitoring and Assessment of Relief and Transition\
    \ (SMART) 2011-2013, MIC 2010. Les indicateurs principaux utilis\xE9s pour l'analyse\
    \ \xE9taient, parmi d'autres, la classification Fewsnet d'ins\xE9curit\xE9 alimentaire,\
    \ le nombre de sondages avec au-dessus de 30% des m\xE9nages en conditions d'ins\xE9\
    curit\xE9 alimentaire et la pr\xE9valence de Malnutrition A\xEFgue Globale (MAG)."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ac69a03cd0ce4da28f90c7872fa59af5/data
  format: null
  id: resource_e1213e96
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Food Insecurity and Malnutrition Trend, 2005-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This layer contains information about the numbers of food insecure\
    \ people - by second-level administrative unit - estimated for the purposes of\
    \ the Integrated Context Analysis (ICA) run in Mali in 2014. Data source: Emergency\
    \ Food Security Analysis (EFSA) 2013. The main indicator used for the analysis\
    \ was the food insecure population for long-term planning. Cette couche contient\
    \ informations regard les nombres de personnes expos\xE9es \xE0 l'ins\xE9curit\xE9\
    \ alimentaire - par unit\xE9 administrative de deuxi\xE8me niveau - employ\xE9\
    es pendant l'Analyse Integr\xE9e du Contexte (AIC) execut\xE9e en Mali en 2014.\
    \ Source des donn\xE9es: Emergency Food Security Analysis (EFSA) 2013. L'indicateur\
    \ principale utilis\xE9 pour l'analyse \xE9tait la population expos\xE9e \xE0\
    \ l'ins\xE9curit\xE9 alimentaire pour la planification \xE0 long-terme."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/21c24452f1fb44e2848b91daa42ee539/data
  format: null
  id: resource_4516412b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mali, 2014 - Estimated Numbers of Food Insecure People, 2013
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_wfp_integratedcontextanalysis_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: 'Mali: Integrated Context Analysis (ICA), 2014'
version: null
vulnerability: null
---

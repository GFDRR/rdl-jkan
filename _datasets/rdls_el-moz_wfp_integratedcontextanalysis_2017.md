---
attributions:
- entity:
    affiliation: null
    email: null
    name: SETSAN (Technical Secretariat for Food Security and Nutrition)
    url: https://data.humdata.org/dataset/wfp_ica_moz_2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VAC (Vulnerability Assessment Committee)
    url: https://data.humdata.org/dataset/wfp_ica_moz_2017
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_moz_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_moz_2017
dataset_id: rdls_el-moz_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_moz_2017]'
details: null
exposure:
- asset_type:
    description: Population density distribution across ICA areas in 2015
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
    description: Agricultural production areas and cereal production volumes 2002-2015
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
  description: The ICA integrates multi-year food security trend data from SETSAN
    and VAC surveys with historical hazard occurrence maps (flood 1975-2012, drought
    1981-2015, cyclone 1930-2000) and agricultural/population exposure data to identify
    sub-national areas where different programme strategies are appropriate for reducing
    food insecurity and climate shock risk.
  sources:
  - id: source_1
    license: null
    name: SETSAN (Technical Secretariat for Food Security and Nutrition)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: VAC (Vulnerability Assessment Committee)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_moz_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by flood hazard recurrence
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Food insecure population affected by drought hazard recurrence
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
    description: Food insecure population affected by cyclone hazard recurrence
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/19304521b4424b7e82ff0d004b2903f9/data
  format: PNG
  id: resource_22e0eb07
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Natural Shocks Hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6cde5ac049fc46d99748de63cd1c428b/data
  format: PNG
  id: resource_d7ebfe8c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Flood Hazard, 1975-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/09e5949e10d44314b332baa8b04a9fa8/data
  format: PNG
  id: resource_46d9de8a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - ICA Areas & Population Density (2015)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the combined natural shock (floods,
    droughts and cyclones) hazard estimated during the Integrated Context Analysis
    (ICA) run in Mozambique in 2017. Data source: Fewsnet 1975-2012, DRFI 2012, INGC,
    HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE) 1981-2015, Fewsnet 1930-2000.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/50dd8036c8ba456b8d01a80cd2d87f6c/data
  format: null
  id: resource_3f62827d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Natural Shocks Hazard
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification resulting
    from the Integrated Context Analysis (ICA) run in Mozambique in 2017, showing
    areas of convergence between high recurrence of food insecurity and propensity
    to natural shocks. It should be noted that, although not being the official categorization
    included in the Technical Paper, the shapefile contains also the different ICA
    categorizations resulting from combining the natural shock hazard score with SETSAN
    and VAC classifications separately.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8e7a200b8f6a4327bfb8a1e14c0d2a04/data
  format: null
  id: resource_cf503cdd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) run in Mozambique in 2017.
    Data source: HQ OSEP GIS Analysis of NASA MODIS, 2001-2012. The main indicator
    used for the analysis was the percentage of district area that experienced deforestation
    in the time window examined.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3915b4d12b93491294f4eef19dfe8f6d/data
  format: null
  id: resource_89be00f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Land Degradation, 2001-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/38fea3c159e040fa94b0f4bd9c8d28b2/data
  format: PNG
  id: resource_eb85a162
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Drought Hazard, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/3e14ef8946b14a509d6f3a71d8cf97fb/data
  format: PNG
  id: resource_43829ed9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - ICA Areas & Land Degradation (2001-2012)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9f5c0248b9144a73abf0576e8cef37a4/data
  format: PNG
  id: resource_3255f1f1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - ICA Areas & Agricultural Production (2002-2015)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fe9e5760044f4dc8b7dba2c2839c9532/data
  format: PNG
  id: resource_1ec3dd57
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Recurrence of Food Insecurity, SETSAN 2006-2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7f57d0821fd04cbbbece32f1d2597cb0/data
  format: PNG
  id: resource_8bb4348f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Recurrence of Food Insecurity, VAC 2012-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/042010e0134c434aa6042f2fc4c1988b/data
  format: PNG
  id: resource_7c35ee80
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Additional Food Insecure Population in case of a Major
    Shock, 2006-2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/23a4adc2ddc543498e7f1093b26cab7c/data
  format: PNG
  id: resource_8df6d955
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Combined Recurrence of Food Insecurity, 2006-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b1fc9a738e5344d691880762a8e594b9/data
  format: PNG
  id: resource_cd1a993a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Percentage of Food Insecure Population for Long-Term
    Planning, 2006-2009-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7a99b571cee84e7b81f60f37b00acfe9/data
  format: PNG
  id: resource_67c2e042
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Cyclone Hazard, 1930-2000
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimates of food insecure
    population for long-term planning and the additional food insecure people in case
    of a major shock. Data source: SETSAN 2006-2009-2013.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8f11b0b16a864e1ba3cbeea34b3be587/data
  format: null
  id: resource_1d34138e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Estimated Numbers of Food Insecure People, 2006-2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the cereal production - by first-level
    administrative area - calculated during the Integrated Context Analysis (ICA)
    run in Mozambique in 2017. Data source: Ministry of Agriculture and Food Security
    (MASA), 2002-2015. The indicator used for the analysis is the quantity of millet,
    rice, sorghum and cassava - expressed in tons.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/aa1be2efc8a747c8abcc78edc52f39d8/data
  format: null
  id: resource_1e4c1a0c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Cereal Production, 2002-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood hazard estimated during
    the Integrated Context Analysis (ICA) run in Mozambique in 2017. Data source:
    Fewsnet 1975-2012, Disaster Risk Financing and Insurance (DRFI), 2012. The indicators
    used for the analysis were the percentage of flood extent and a qualitative classification
    of the district at high or very high flood risk. It should be noted that the analysis
    did not consider information about the flood frequency and that, in the last 5
    years, flood patterns are changing and affecting the northern part of the country,
    which is not registering extreme flood events anymore.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5e125fab859b4287827eea030d39f08e/data
  format: null
  id: resource_bea3f281
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Flood Hazard, 1975-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the cyclone hazard estimated
    during the Integrated Context Analysis (ICA) run in Mozambique in 2017. Data source:
    Fewsnet, 1930-2000. The indicator used for the analysis was the average frequency
    of cyclone events.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/de1347a9573f46e99e5f40a45163caee/data
  format: null
  id: resource_d77826ae
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Cyclone Hazard, 1930-2000
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/37fded20bd77442d8f91bba15b5a58dc/data
  format: PNG
  id: resource_d8bc635c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - ICA Areas & Prevalence of Stunting (2013)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of food insecurity
    estimated during the Integrated Context Analysis (ICA) run in Mozambique in 2017.
    Data source: Food Security and Nutrition baseline data (SETSAN) 2006-2009-2013,
    Mozambique Vulnerability Assessment Committee (VAC) 2012-2016. The main indicator
    used for the analysis was, for both the assessments used, the Food Consumption
    Score (FCS), considering households with poor and borderline food insecurity and
    a threshold set to 20% given that this highlights areas where at least 1 out of
    5 households is food insecure.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/39686cb8354f490e951e9b0e4c4feb7e/data
  format: null
  id: resource_4f40c5e7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Recurrence of Food Insecurity, 2006-2016
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought hazard estimated
    during the Integrated Context Analysis (ICA) run in Mozambique in 2017. Data source:
    HQ VAM Analysis of CHIRPS Rainfall Estimates (RFE), 1981-2015, National Institute
    of Disaster Management (INGC). The indicators used for the analysis were the number
    of poor growing seasons and the drought hazard classification provided by INGC.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2d4aa73a3eba4e0d9627e7e007b3db05/data
  format: null
  id: resource_101a4b7c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Drought Hazard, 1981-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the malnutrition levels - by
    first-level administrative unit - observed during the Integrated Context Analysis
    (ICA) run in Mozambique in 2017. Data source: SETSAN, 2013. The key indicator
    used for the analysis was the prevalence of stunting in children aged under 5
    years, classified according to the classification for assessing severity of malnutrition
    provided by the World Health Organization (WHO). It should be noted that the shapefile
    also includes the figures about the prevalence of wasting in children aged under
    5 years, indicator which has not been considered in the final version of the Technical
    Paper.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/774982f9dae74d43a2cf3bb7789f7b90/data
  format: null
  id: resource_c54004c3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Prevalence of Stunting, 2013
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in Mozambique in 2017. The analysis brings together the historical
    risk of natural shocks (floods, droughts and cyclones) and the recurrence of high
    food insecurity with other key contextual information to provide broad programmatic
    strategies by second-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/99d3f39c880b40eabedc78971838aa07/data
  format: null
  id: resource_631a7642
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Mozambique, 2017 - Technical Paper
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-moz_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Mozambique: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_phl_2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_phl_2014
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_phl_2014
dataset_id: rdls_el-phl_wfp_integratedcontextanalysis_2014
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_phl_2014]'
details: null
exposure:
- asset_type:
    description: Population living below the poverty line at sub-national level, 2012
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
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend analysis with mapped
    natural shock risk data (flood, landslide, tropical storm occurrence) at sub-national
    level to produce a strategic vulnerability assessment. Historical hazard occurrence
    records (2002-2012) and poverty/food insecurity data (2006-2012) were spatially
    integrated to identify areas where different programme interventions are appropriate
    for reducing food insecurity and climate shock risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_phl_2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and vulnerability to flood hazards in sub-national
      areas
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and vulnerability to landslide hazards in sub-national
      areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and vulnerability to tropical storm hazards in sub-national
      areas
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
        type: total
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
  description: 'This layer contains information about the average landslide risk -
    by second-level administrative area - used for the purposes of the Integrated
    Context Analysis (ICA) run in the Philippines in 2014. Data source: National Household
    Targeting System and Mines and Geosciences Bureau. The main indicator used for
    the analysis was the average flandslide risk by barangay reaggregated by province
    level.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/bfeb194c45394c02abda71a90e1ccf8b/data
  format: null
  id: resource_57122bf7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Average Landslide Risk, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the average flood risk - by
    second-level administrative area - used for the purposes of the Integrated Context
    Analysis (ICA) run in the Philippines in 2014. Data source: National Household
    Targeting System and Mines and Geosciences Bureau. The main indicator used for
    the analysis was the average flood risk by barangay reaggregated by province level.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/e4e63b9d704d454f92311d8334c68622/data
  format: null
  id: resource_863cfbd6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Flood Risk, 2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final classification resulting
    from the Integrated Context Analysis (ICA) run in the Philippines in 2014, showing
    the areas of convergence between recurrence of poverty incidence and propensity
    to natural shocks (floods, tropical storms, landslides and tree cover change).
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/82324dfd5dc0460b9680e12ecbc100bb/data
  format: null
  id: resource_32282285
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - ICA Categories & Focus Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This document contains the results of the Integrated Context Analysis
    (ICA) conducted in the Philippines in 2014. The analysis brings together the historical
    risk of natural shocks (floods, tropical storms, landslides and tree cover changes)
    and the recurrence of poverty incidence with other key contextual information
    to provide broad programmatic strategies by first-level administrative area.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b3e0bde1bfdd447587d7279d2a4f81b7/data
  format: null
  id: resource_b4c4b8cc
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Technical Paper & Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the recurrence of poverty incidence
    - by second-level administrative area - observed during the Integrated Context
    Analysis (ICA) run in the Philippines in 2014. Data sources: Philippines National
    Statistical Coordination Board (NSCB), 2006-2012. It should be noted that, in
    absence of national food security information, poverty data has been used as a
    proxy to food insecurity - assuming that families below the poverty line are likely
    to be food insecure. Also, in the Philippines official methodology, the poverty
    line may be viewed as the minimum income required to meet food requirements as
    well as non-food basic needs. The main indicator used for the analysis was the
    recurrence of poverty incidence, with a threshold set to 30% of the families to
    represent 1 out of 3 people below the poverty line.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/ac2ef6098d7648809ad051fd01ca81d0/data
  format: null
  id: resource_9c0af5a1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Recurrence of Poverty Incidence, 2006-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the occurrence of tropical storms
    above Category 3 - according to the Saffir-Simpson scale and by second-level administrative
    area - used for the purposes of the Integrated Context Analysis (ICA) run in the
    Philippines in 2014. Data source: National Oceanic and Atmospheric Administration
    (NOAA) IBTrACS, 2002-2012. The main indicator used for the analysis was the number
    of times that a province was hit, in the time frame of interest, by a tropical
    storm above Category 3.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d0e3961581b14cf485de352e8c967b37/data
  format: null
  id: resource_b649f95c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Tropical Storm (above Category 3) Occurrence, 2002-2012
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the changes in tree cover density
    - by second-level administrative area - estimated during the Integrated Context
    Analysis (ICA) run in the Philippines in 2014. Data source: Landsat Vegetation
    Continuous Fields (VCF), 2000-2010. It should be noted that, in absence of livelihood
    data, land cover was used as a proxy for rural livelihoods. The main indicator
    used for the analysis was the average provincial trend of tree cover change in
    the last ten years.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/222d4bb7af4f4972bff0b865273692f9/data
  format: null
  id: resource_077aad64
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Tree Cover Change, 2000-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the estimated numbers of people
    living below the poverty line used for the purposes of the Integrated Context
    Analysis (ICA) run in the Philippines in 2014. Data source: Philippines National
    Statistical Coordination Board (NSCB), 2012.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2ff8aff8a2d843b185dfb48e877564fe/data
  format: null
  id: resource_c60318e9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Philippines, 2014 - Estimated Numbers of People living below the Poverty
    Line, 2012
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-phl_wfp_integratedcontextanalysis_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: 'Philippines: Integrated Context Analysis (ICA), 2014'
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_tcd_2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tcd_2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tcd_2018
dataset_id: rdls_he-tcd_wfp_integratedcontextanalysis_2018
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_tcd_2018]'
details: null
exposure:
- asset_type:
    description: Livelihood zones mapped by predominant agricultural and pastoral
      activities
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population dependent on food security and livelihoods in mapped zones
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
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
  type: drought
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend analysis with climate-related
    natural shock risk data through consultations and geographic information systems
    to produce sub-national livelihood zone maps. These maps identify areas where
    different programme strategies (safety nets vs. shock recovery) are appropriate
    for reducing food insecurity and climate risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_tcd_2018
  rel: source
loss: null
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
  description: "This layer contains information about the most predominant livelihood\
    \ zones - by second-level administrative area - identified during the Integrated\
    \ Context Analysis (ICA) run in Chad in 2017. The analysis was a joint effort\
    \ between the Regional Bureau in Dakar (RBD) and the HQ GIS Unit and Programme\
    \ division. Data source: Fewsnet, 2011. Cette couche contient informations regard\
    \ les zones de moyens d'existence pr\xE9dominant - par unit\xE9 administrative\
    \ de deuxi\xE8me niveau - identifi\xE9es pendant l'Analyse Integr\xE9e du Contexte\
    \ (AIC) execut\xE9e en Tchad en 2017. L'analyse a \xE9t\xE9 execut\xE9e gr\xE2\
    ce \xE0 la collaboration entre le Bureau R\xE9gional de Dakar (RBD), l'unit\xE9\
    \ GIS et la division de Programme au quartier g\xE9n\xE9rale du PAM. Source des\
    \ donn\xE9es: Fewsnet, 2011."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/27ea3654eaaf47f0baa1d2a7ed99379b/data
  format: null
  id: resource_4c514229
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Chad, 2017 - Most Predominant Livelihood Zones, 2011
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tcd_wfp_integratedcontextanalysis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Chad: Integrated Context Analysis (ICA), 2018'
version: null
vulnerability: null
---

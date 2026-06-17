---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsamboh_20220304
description: 'UNOSAT code: TC20220221MDG This map illustrates satellite-detected surface
  waters in Ambohimahasoa, Isandra, Lalangina, And Vohibato Districts, Haute Matsiatra
  Region, Madagascar as observed from a Sentinel-2 image acquired on 24 February 2022
  at 10:00 local time. Within the analyzed area about 2,000 km2, a total of about
  130 km2 of lands appear to be flooded. Based on Worldpop population data and the
  detected surface waters, about 17,500 people are potentially exposed or living close
  to flooded areas. This is a preliminary analysis that has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 24 February 2022 and identified surface water extents through visual interpretation\
    \ and change detection methods. Detected water polygons (130 km\xC2\xB2 total)\
    \ were intersected with WorldPop gridded population data to estimate approximately\
    \ 17,500 people potentially exposed to flooded areas in the three districts of\
    \ Haute Matsiatra Region."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-ambohimahasoa-lalangina-and-vohibato-districts-madagascar-as-of-24-februa
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to detected flood waters from satellite observation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected water extents in Ambohimahasoa, Lalangina, and Vohibato
    Districts, Madagascar as of 24 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_gdb.zip
  format: Geodatabase
  id: resource_27274068
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Ambohimahasoa, Lalangina, and Vohibato
    Districts, Madagascar as of 24 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_SHP.zip
  format: null
  id: resource_f0468ae2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsamboh_20220304
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-04'
temporal_resolution: null
title: Satellite detected water extents in Ambohimahasoa, Lalangina, and Vohibato
  Districts, Madagascar as of 24 February 2022
version: null
vulnerability: null
---

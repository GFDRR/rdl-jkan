---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-wajir-county-kenya-2801
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-wajir-county-kenya-2801
dataset_id: rdls_hel-ken_unosat_detectedwateroverwajircou_20180515
description: 'This map illustrates satellite-detected flood water extent over Wajir
  county, Kenya. The analysis was conducted by analyzing Sentinel-1 imagery acquired
  on the 4 May 2018. Within the analysis extent, around 111,800 ha of land appears
  to be inundated and more than 46,300 people are living inside this flood water extent.Within
  the analysis extent, the sub county of Wajir West presents 68,000 ha of land inundated
  and more than 6,100 people potentially affected while Wajir South presents ~ 26,300
  ha of land inundated and ~ 19,000 people potentially affected. It is likely that
  flood waters have been systematically underestimated along highly vegetated areas
  along main river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-wajir-county-kenya-2801]'
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
    description: Population living within satellite-detected flood water extent in
      Wajir county
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
  description: UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 4 May
    2018 over Wajir county, Kenya, using change detection methodology to identify
    satellite-detected water extent. The resulting flood water polygon was quantified
    for area (111,800 ha total) and intersected with population data to estimate affected
    population counts (46,300 people total) by sub-county administrative divisions.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-over-wajir-county-kenya-2801
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by satellite-detected flood inundation
      in Wajir county
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
  description: Satellite detected water over Wajir county, Kenya (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/KE/FL20180508KEN/FL20180508KEN_shp.zip
  format: null
  id: resource_723497d2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180508KEN_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwateroverwajircou_20180515
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-15'
temporal_resolution: null
title: Satellite detected water over Wajir county, Kenya
version: null
vulnerability: null
---

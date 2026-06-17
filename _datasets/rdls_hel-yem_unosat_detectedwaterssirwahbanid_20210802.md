---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 radar imagery
    url: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020
dataset_id: rdls_hel-yem_unosat_detectedwaterssirwahbanid_20210802
description: 'UNOSAT code: FL20210729YEM This map illustrates satellite-detected surface
  waters over Sirwah, Bani Dabyan, and Al Jubah districts of Yemen as observed from
  a Sentinel-1 radar image acquired on 26 July 2021. Within the analyzed area of about
  3,800 km2, a total of about 6.5 km2 of lands appear to be flooded. Based on Worldpop
  population data and the detected surface waters, about 1,800 people may be potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR- UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020]'
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
    description: Population potentially exposed or living close to satellite-detected
      flooded areas derived from WorldPop data
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts performed change detection analysis on Sentinel-1 radar
    imagery acquired on 26 July 2021 to identify surface water extent in three districts
    of Yemen. Detected water polygons were intersected with WorldPop population data
    to estimate approximately 1,800 people potentially exposed to flooded areas. This
    preliminary analysis has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 radar imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-in-sirwah-bani-dabyan-and-al-jubah-districts-of-yemen-as-of-26-july-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas based on spatial
      intersection of detected surface waters and population distribution
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
  description: Satellite detected waters in Sirwah, Bani Dabyan, and Al Jubah districts
    of Yemen as of 26 July 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_gdb.zip
  format: Geodatabase
  id: resource_4a65eb81
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Sirwah, Bani Dabyan, and Al Jubah districts
    of Yemen as of 26 July 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_shp.zip
  format: null
  id: resource_c33f6fc0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-yem_unosat_detectedwaterssirwahbanid_20210802
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-02'
temporal_resolution: null
title: Satellite detected waters in Sirwah, Bani Dabyan, and Al Jubah districts of
  Yemen as of 26 July 2020
version: null
vulnerability: null
---

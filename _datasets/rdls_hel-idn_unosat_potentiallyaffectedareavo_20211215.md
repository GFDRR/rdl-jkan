---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i
dataset_id: rdls_hel-idn_unosat_potentiallyaffectedareavo_20211215
description: 'UNOSAT code: VO20211205IDN This map illustrates the potentially affected
  areas by Lahar and Pyroclastic density currents (PDCs) including geological information
  of Mount Semeru, Java province, Indonesia as detected by satellite images acquired
  after the eruption of the Mount Semeru on 4 Dec 2021. UNITAR-UNOSAT analysis used
  Pleiades images acquired on 10 & 11 Dec 2021 to estimate the affected area by Lahar
  and Pyroclastic density currents. Within the analyzed area, about 3,220 ha appear
  to be affected. Based on Worldpop population data and affected area by Lahar and
  pyroclastic density currents, about 8,400 people are potentially exposed or living
  close to pyroclastic density area. In addition, base on Esri 2020 Land Cover, potentially
  affected in tree area ~2,100ha, scrub/shrub area ~ 400 ha, cropland ~ 165 ha, built
  area ~ 140 ha. Important note: Pyroclastic density currents (PDCs) are perhaps the
  most hazardous events to local areas during explosive volcanic eruptions. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i]'
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
    description: Residential population in areas affected by lahar and pyroclastic
      density currents based on WorldPop data
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
    description: Land area affected by volcanic hazards including lahar and pyroclastic
      density currents
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: lahar
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-eruption Pleiades satellite
    imagery acquired on 10-11 December 2021 to detect and delineate areas affected
    by lahar and pyroclastic density currents from the Mount Semeru eruption. WorldPop
    population data was overlaid on the affected area polygons to estimate potentially
    affected population. The resulting dataset provides post-event hazard extent and
    exposure estimates for volcanic hazards in Java Province.
  sources:
  - id: source_1
    license: null
    name: Pleiades satellite imagery
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
- href: https://data.humdata.org/dataset/potentially-affected-area-by-volcanic-eruption-effect-of-the-4-dec-2021-in-java-province-i
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct area loss from lahar and pyroclastic density current inundation
      affecting approximately 3,220 hectares
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Potentially affected area by volcanic eruption effect of the 4 Dec
    2021 in Java Province, Indonesia as of 10&11 Dec 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ID/VO20211205IDN/VO20211205IDN_gdb.zip
  format: Geodatabase
  id: resource_3c5a15c7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20211205IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Potentially affected area by volcanic eruption effect of the 4 Dec
    2021 in Java Province, Indonesia as of 10&11 Dec 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ID/VO20211205IDN/VO20211205IDN_shp.shp
  format: null
  id: resource_6d419058
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20211205IDN_shp.shp
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_potentiallyaffectedareavo_20211215
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-12-15'
temporal_resolution: null
title: Potentially affected area by volcanic eruption effect of the 4 Dec 2021 in
  Java Province, Indonesia as of 10&11 Dec 2021
version: null
vulnerability: null
---

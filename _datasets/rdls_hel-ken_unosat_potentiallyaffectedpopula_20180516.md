---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-population-by-flooding-in-eastern-kenya-2804
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-population-by-flooding-in-eastern-kenya-2804
dataset_id: rdls_hel-ken_unosat_potentiallyaffectedpopula_20180516
description: 'This map illustrates potentially affected population by flooding in
  the eastern sub counties of Kenya. The analysis was conducted by analyzing Sentinel-1
  imagery acquired on the 4 May 2018. Within the analysis extent, more than 200,000
  people are potentially affected by the floods. Magarini sub county in Kilifi County,
  is the one with more than 40,000 people living inside flood affected areas, followed
  by Dadaab, Wajir South, Garsen and Malindi sub counties. Note that some sub counties
  have been partially analyzed depending on the area covered by satellite imagery.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas, along main river banks and within built-up urban areas because
  of the special characteristics of the satellite data used. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-population-by-flooding-in-eastern-kenya-2804]'
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
    description: Population living within flood-affected areas identified through
      satellite imagery analysis
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
  - analysis_type: probabilistic
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
  description: UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 4 May
    2018 to detect flood extent through change detection analysis. Flood-affected
    areas were mapped as polygons with area measurements. Population exposure was
    estimated by intersecting flood extent polygons with population distribution data,
    yielding affected population counts by sub-county.
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
- href: https://data.humdata.org/dataset/potentially-affected-population-by-flooding-in-eastern-kenya-2804
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding in eastern Kenya sub-counties based
      on flood extent mapping
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
  description: Potentially affected population by flooding in eastern Kenya (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/KE/FL20180508KEN/FL20180508KEN_shp.zip
  format: null
  id: resource_782394b1
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
slug: rdls_hel-ken_unosat_potentiallyaffectedpopula_20180516
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
  start: '2018-05-16'
temporal_resolution: null
title: Potentially affected population by flooding in eastern Kenya
version: null
vulnerability: null
---

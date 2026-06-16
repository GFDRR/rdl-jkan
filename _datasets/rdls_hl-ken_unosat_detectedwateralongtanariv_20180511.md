---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-galole-garsen-sub-counties-tanariver-county-kenya-2799
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-galole-garsen-sub-counties-tanariver-county-kenya-2799
dataset_id: rdls_hl-ken_unosat_detectedwateralongtanariv_20180511
description: 'This map illustrates satellite-detected flood water extent along Tana
  River, Galole and Garsen sub counties, Tana River county, Kenya. The analysis was
  conducted by analyzing Sentinel-1 imagery acquired on the 4 May 2018. The analysis
  extent is focused on the river bed of Tana, the surrounding land between the primary
  road and the limit of the Tana River boundary, specifically where the population
  is concentrated. Within the analysis extent, around 22,700 ha of land appears to
  be inundated and more than 21,600 people are living inside this flood water extent.
  It is likely that flood waters have been systematically underestimated along highly
  vegetated areas along main river banks and within built-up urban areas because of
  the special characteristics of the satellite data used. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-galole-garsen-sub-counties-tanariver-county-kenya-2799]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-1 synthetic aperture radar (SAR) imagery acquired on 4 May
    2018 was analyzed by UNOSAT analysts to detect surface water extent along the
    Tana River floodplain in Galole and Garsen sub-counties. Change detection and
    image interpretation techniques were applied to delineate inundated areas, with
    analysis focused on the river bed and surrounding populated land between the primary
    road and the Tana River boundary. Population exposure within the flood extent
    was estimated at over 21,600 people across approximately 22,700 ha of inundated
    land.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-galole-garsen-sub-counties-tanariver-county-kenya-2799
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people (>21,600) living within the satellite-detected
      flood water extent along Tana River
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Satellite detected water along Tana River, Galole & Garsen sub counties,
    TanaRiver county, Kenya (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/KE/FL20180508KEN/FL20180508KEN_shp.zip
  format: null
  id: resource_153f8494
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180508KEN_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-ken_unosat_detectedwateralongtanariv_20180511
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
  start: '2018-05-11'
temporal_resolution: null
title: Satellite detected water along Tana River, Galole & Garsen sub counties, TanaRiver
  county, Kenya
version: null
vulnerability: null
---

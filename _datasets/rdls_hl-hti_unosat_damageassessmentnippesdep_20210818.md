---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nippes-department-haiti-as-of-16-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-nippes-department-haiti-as-of-16-august-2021
dataset_id: rdls_hl-hti_unosat_damageassessmentnippesdep_20210818
description: 'UNOSAT code: EQ20210814HTI This map illustrates potentially damaged
  structures/buildings in Nippes department of Haiti as detected by using a satellite
  image acquired after the earthquake. UNOSAT analysis used a Worldview-2 image acquired
  on 14 & 16 August 2021, a Worldview-1 image acquired on 15 August 2021, a Worldview-3
  image acquired on 16 August 2021, and Pleiades images acquired on 15 & 16 August
  2021, as a post-event images. Within the analyzed area, UNOSAT identified 73 damaged
  structures and 125 potentially damaged structures. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-nippes-department-haiti-as-of-16-august-2021]'
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
    earthquake:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal high-resolution satellite imagery
    (Worldview and Pleiades sensors) acquired immediately after the 14 August 2021
    earthquake to detect structural changes and classify buildings as damaged or potentially
    damaged. Building footprints and damage classifications were manually interpreted
    and vectorized into geodatabase and shapefile formats for the Nippes department
    study area.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-nippes-department-haiti-as-of-16-august-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment identifying 73 confirmed damaged
      and 125 potentially damaged structures from earthquake ground motion
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: Damage Assessment in Nippes department, Haiti as of 16 August 2021
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_gdb.zip
  format: Geodatabase
  id: resource_f2ac20ea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Nippes department, Haiti as of 16 August 2021
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_shp.zip
  format: null
  id: resource_b207c091
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-hti_unosat_damageassessmentnippesdep_20210818
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-18'
temporal_resolution: null
title: Damage Assessment in Nippes department, Haiti as of 16 August 2021
version: null
vulnerability: null
---

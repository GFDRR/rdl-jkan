---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/building-damage-assessment-in-crawford-village-black-river-district-saint-elizabeth-parish
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-crawford-village-black-river-district-saint-elizabeth-parish
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-crawford-village-black-river-district-saint-elizabeth-parish
dataset_id: rdls_hl-jam_unosat_buildingdamageassessmentc_20251030
description: 'UNOSAT code: TC20251026HTI, GDACS ID: 1001230 This map illustrates the
  structures/buildings damaged by Tropical Cyclone MELISSA-25. The analysis focuses
  on Crawford Village, Black River District, Saint Elizabeth Parish, as of 29 October
  2025, where damage was detected using a WorldView-2 very high-resolution satellite
  image acquired on 29 October 2025. UNOSAT identified approximately 1,089 buildings
  as 100% damaged. This is a preliminary analysis and has not yet been validated in
  the field. Ground verification is encouraged, and feedback can be sent to the United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assessment-in-crawford-village-black-river-district-saint-elizabeth-parish]'
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event WorldView-2 satellite
    imagery to detect structural damage in Crawford Village caused by Tropical Cyclone
    MELISSA-25. Building footprints were identified and classified by damage severity,
    with approximately 1,089 structures mapped as 100% damaged as of 29 October 2025.
    This preliminary assessment was conducted without field validation.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/building-damage-assessment-in-crawford-village-black-river-district-saint-elizabeth-parish
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone MELISSA-25, with 1,089
      structures assessed as 100% damaged
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Jamaica - Building Damage Assessment in Crawford Village, Black River
    District, Saint Elizabeth Parish as of 29 October 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4211/TC20251027JAM_GDB.zip
  format: Geodatabase
  id: resource_bcde896b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20251027JAM_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica - Building Damage Assessment in Crawford Village, Black River
    District, Saint Elizabeth Parish as of 29 October 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4211/TC20251027JAM_SHP.zip
  format: null
  id: resource_6426166a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20251027JAM_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-jam_unosat_buildingdamageassessmentc_20251030
spatial:
  bbox: null
  centroid: null
  countries:
  - JAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-10-30'
temporal_resolution: null
title: Jamaica - Building Damage Assessment in Crawford Village, Black River District,
  Saint Elizabeth Parish as of 29 October 2025
version: null
vulnerability: null
---

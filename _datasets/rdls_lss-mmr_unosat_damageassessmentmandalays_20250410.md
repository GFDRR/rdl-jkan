---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus EMS
    url: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ICube-SERTIT
    url: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
dataset_id: rdls_lss-mmr_unosat_damageassessmentmandalays_20250410
description: "UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map illustrates the\
  \ density of damaged buildings affected by the March 28, 2025, earthquake in Mandalay.\
  \ The analysis focuses on Mandalay & Sagaing Districts. Within the map extent of\
  \ about 2,100 km\xB2, UNOSAT, Copernicus EMS and ICube-SERTIT observed a total of\
  \ 4,764 destroyed and damaged structures & 4,369 potentially damaged structures.\
  \ Within Mandalay City boundary of about 110km\xB2, a total of 1,076 structures\
  \ are observed as destroyed and damaged, & a total of 519 structures are observed\
  \ as potentially damaged. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025]"
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Post-event damage assessment derived from satellite imagery acquired
    after the March 28, 2025 earthquake, with analysts comparing pre- and post-event
    images to identify structural damage. UNOSAT, Copernicus EMS, and ICube-SERTIT
    jointly analyzed satellite data to classify buildings as destroyed, damaged, or
    potentially damaged across Mandalay and Sagaing Districts.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Copernicus EMS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ICube-SERTIT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-mandalay-sagaing-districts-myanmar-as-of-03-april-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the March 28, 2025 earthquake
      in Mandalay and Sagaing Districts
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
  description: Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03
    April 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4098/GDB.zip
  format: Geodatabase
  id: resource_b66841da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03
    April 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4098/SHP.zip
  format: null
  id: resource_2983fd8f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03
    April 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4098/UNOSAT_EQ20250328MMR_DamageAssessment_Mandalay_SERTIT_Copernicus_10Apr2025.xlsx
  format: null
  id: resource_fdde6779
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_EQ20250328MMR_DamageAssessment_Mandalay_SERTIT_Copernicus_10Apr2025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_damageassessmentmandalays_20250410
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-10'
temporal_resolution: null
title: Damage Assessment in Mandalay & Sagaing Districts, Myanmar as of 03 April 2025
version: null
vulnerability: null
---

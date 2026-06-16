---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-
dataset_id: rdls_hel-syr_unosat_wildfiresqastalmaafrabeek_20250709
description: "UNOSAT code: FR20250707SYR, GDACS ID: 1024188 This map illustrates satellite-detected\
  \ burned areas in Qastal Maaf, Rabee'a, and Kasab Sub-districts, Latakia Governorate,\
  \ Syria, based on Pleiades imagery acquired on 8 July 2025 at 11:48 local time.\
  \ Within the analyzed area of approximately 700 km\xB2, around 100 km\xB2 of land\
  \ appears to be potentially burned. Based on WorldPop population data and the extent\
  \ of the burned areas, an estimated 5,500 people are potentially exposed or living\
  \ in close proximity to the affected zones. In addition, approximately 2,400 buildings\
  \ were potentially exposed to fires. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-]"
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
    description: Estimated 5,500 people potentially exposed or living in close proximity
      to wildfire-affected zones based on WorldPop data
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
    description: Approximately 2,400 buildings in the wildfire-affected areas
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Pleiades satellite imagery acquired on 8\
    \ July 2025 to detect burned areas through change detection analysis, identifying\
    \ approximately 100 km\xB2 of burned land. Burned area polygons were intersected\
    \ with WorldPop gridded population data and building footprints to estimate exposure\
    \ and potential impacts in Qastal Maaf, Rabee'a, and Kasab Sub-districts, Latakia\
    \ Governorate, Syria."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-qastal-maaf-rabee-a-and-kasab-sub-district-latakia-governorate-syria-as-of-8-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to wildfire-affected zones based on satellite-detected
      burned areas and proximity analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings in wildfire-affected areas identified through satellite
      imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_2
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
  description: Wildfires in Qastal Maaf, Rabee'a and Kasab Sub-district, Latakia Governorate,
    Syria as of 8 July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4146/FR20250707SYR_gdb.zip
  format: Geodatabase
  id: resource_483e3a52
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20250707SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires in Qastal Maaf, Rabee'a and Kasab Sub-district, Latakia Governorate,
    Syria as of 8 July 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4146/FR20250707SYR_SHP.zip
  format: null
  id: resource_04ca3f04
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20250707SYR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires in Qastal Maaf, Rabee'a and Kasab Sub-district, Latakia Governorate,
    Syria as of 8 July 2025 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4146/PopulationExposure_FR20250707SYR_Latakia_8July2025.xlsx
  format: null
  id: resource_d37d2998
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PopulationExposure_FR20250707SYR_Latakia_8July2025.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-syr_unosat_wildfiresqastalmaafrabeek_20250709
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-09'
temporal_resolution: null
title: Wildfires in Qastal Maaf, Rabee'a and Kasab Sub-district, Latakia Governorate,
  Syria as of 8 July 2025
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: Vantor (formerly Maxar)
    url: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NOAA NGS
    url: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica
dataset_id: rdls_hel-jam_msftai_hurricanemelissabuildingd_2025
description: 'We ran our damage assessment AI models on images provided by Vantor
  (formerly Maxar) and NOAA NGS and have mapped out the affected buildings. If your
  organization would benefit from access to the underlying data in this report, please
  reach out to me. We are committed to sharing this information to support ongoing
  recovery efforts.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
  Any building classified as >0% damaged likely has nearby debris and should be further
  inspected.
exposure:
- asset_type:
    description: Building footprints and inventory mapped across affected areas in
      Jamaica
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Satellite imagery from Vantor and NOAA NGS was processed through Microsoft's
    damage assessment AI model to automatically detect and classify building damage
    from Hurricane Melissa in Jamaica. The model outputs were compiled into geopackage
    files containing building footprints with damage classifications.
  sources:
  - id: source_1
    license: null
    name: Vantor (formerly Maxar)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: NOAA NGS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Microsoft AI for Good Lab
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-melissa-building-damage-assessment-in-jamaica
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Hurricane Melissa assessed via AI analysis
      of satellite imagery
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
  description: Results that outline the building damage assessment footprints that
    covers some parts of St.Elizabeth parish on 11/02/2025 using NOAA NGS imagery
    (flight 20251102a). Out of a total of 30,545 building footprints in the study
    area, our model predicted that 19,811 (64.8%) were damaged to some extent. Comparing
    the model results to independent labels, we estimate the model has a recall of
    76% and precision of 91%.
  download_url: https://data.humdata.org/dataset/04c4bf06-511e-4009-9c03-4ec97334d944/resource/4dc46518-9428-49c2-9750-35e6d5777b07/download/20251102a_visual_predictions_final.gpkg
  format: null
  id: resource_4dc46518
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251102a_visual_predictions_final.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Results that outline the building damage assessment footprints that
    covers some parts of Wesmoreland parish on 11/01/2025 using NOAA NGS imagery (flight
    20251101a). Out of a total of 34,403 building footprints in the study area, our
    model predicted that 21,119 (61.4%) were damaged to some extent.
  download_url: https://data.humdata.org/dataset/04c4bf06-511e-4009-9c03-4ec97334d944/resource/41697efc-4c1a-4882-95eb-7fef2c96eefc/download/20251101a_visual_predictions_final.gpkg
  format: null
  id: resource_41697efc
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251101a_visual_predictions_final.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Results that outline the building damage assessment footprints that
    covers some parts of St.James parish on 10/31/2025 using Vantor imagery. Model
    finds 31,370 buildings damaged out of 44,407 non-cloudy.
  download_url: https://data.humdata.org/dataset/04c4bf06-511e-4009-9c03-4ec97334d944/resource/f030920d-3ece-415c-8e5e-a8775564d2e5/download/melissa_20251031_103001011d843000_visual_buildings_results.gpkg
  format: null
  id: resource_f030920d
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: melissa_20251031_103001011D843000_visual_buildings_results.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results that outline the building damage assessment footprints that
    covers 1500kms2 that intersect with St.Elizabeth parish on 10/29/2025 using Vantor
    imagery. Key findings: - 42,480 buildings assessed in western Jamaica - 32,848
    buildings (76.4%) showed some degree of damage - 64,652 buildings could not be
    analyzed due to cloud cover Methodology: We independently labeled 193 of the footprints
    (with an area greater than 50 square meters) from the source imagery and found
    that 86 were uncloudy and able to be assessed as ''damaged'' or ''undamaged''**.
    Comparing the model results to these labels we estimate the model has a recall
    of 96.2% and precision of 82.2%. Extrapolating these results to the set of building
    footprints with area greater than 50 square meters (n=51,086) we estimate 31,483
    to be damaged (61.6%) with a 95% CI of [26,206 to 36,760]. **By undamaged we mean
    intact, roof on. It is impossible to assess structural damage from overhead imagery
    and these results do not substitute for a ground level building assessment.'
  download_url: https://data.humdata.org/dataset/04c4bf06-511e-4009-9c03-4ec97334d944/resource/e82f0ef4-87d5-4fce-baec-cd8129e37ffb/download/melissa_1_all_buildings_results.gpkg
  format: null
  id: resource_e82f0ef4
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: melissa_1_all_buildings_results.gpkg
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-jam_msftai_hurricanemelissabuildingd_2025
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
  end: '2025-11-02'
  start: '2025-10-29'
temporal_resolution: null
title: 'Hurricane Melissa: Building Damage Assessment in Jamaica'
version: null
vulnerability: null
---

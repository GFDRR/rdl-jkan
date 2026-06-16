---
attributions:
- entity:
    affiliation: null
    email: null
    name: "IDEAM (Instituto de Hidrolog\xEDa, Meteorolog\xEDa y Estudios Ambientales)"
    url: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022
dataset_id: rdls_hl-col_immap_olainvernalen2022
description: "Estas bases contienen la informaci\xF3n de las alertas hidrol\xF3gicas\
  \ reportadas por el IDEAM y eventos por desastres de origen natural reportados por\
  \ la UNGRD en Colombia, con un periodo de tiempo de enero a octubre 2022.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022]"
details: null
exposure: []
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
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Hydrological alert data from IDEAM monitoring systems were integrated
    with disaster event records from UNGRD's national registry to document the 2022
    winter season flood impacts in Colombia. The dataset combines observed hazard
    alerts with post-event impact assessments to characterize flood occurrence and
    affected populations.
  sources:
  - id: source_1
    license: null
    name: "IDEAM (Instituto de Hidrolog\xEDa, Meteorolog\xEDa y Estudios Ambientales)"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ola-invernal-en-colombia-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from natural disaster events including floods
      reported by UNGRD
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene la informaci\xF3n de las alertas hidrol\xF3gicas\
    \ reportadas por el IDEAM de todos los lunes de cada mes entre enero a diciembre\
    \ en Colombia 2022."
  download_url: https://data.humdata.org/dataset/276548f8-e4fa-4173-ad43-ab677a829335/resource/3e0bf13f-54ff-4c6e-8a62-a8f57944df64/download/ideam-alertas-hidrologicas-enero-a-diciembre-2022.xlsx
  format: null
  id: resource_3e0bf13f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "IDEAM - Alertas hidrol\xF3gicas enero a diciembre 2022.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene la informaci\xF3n de los eventos por desastres\
    \ de origen natural, ocurridos entre los meses de enero a diciembre en Colombia\
    \ 2022."
  download_url: https://data.humdata.org/dataset/276548f8-e4fa-4173-ad43-ab677a829335/resource/be067065-5be4-4da3-a090-972e8a5ee1de/download/ungrd-eventos-ocurridos-enero-a-diciembre-2022.xlsx
  format: null
  id: resource_be067065
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNGRD - Eventos ocurridos enero a diciembre 2022.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-col_immap_olainvernalen2022
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Ola invernal en Colombia 2022
version: null
vulnerability: null
---

---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/cameroun-analyse-analyse-ipc-de-la-malnutrition-aigue
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/cameroun-analyse-analyse-ipc-de-la-malnutrition-aigue
creator:
  affiliation: null
  email: null
  name: IPC
  url: https://data.humdata.org/dataset/cameroun-analyse-analyse-ipc-de-la-malnutrition-aigue
dataset_id: rdls_lss-cmr_hdx_malnutritionaigue_2023
description: "Ce jeu de donn\xE9es pr\xE9sente un tableau de population d\xE9taillant\
  \ la situation actuelle pour les zones analys\xE9es, incluant 32 d\xE9partements,\
  \ 4 r\xE9gions et des sites de r\xE9fugi\xE9s centrafricains et nig\xE9rians pour\
  \ la p\xE9riode 2023-2024.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cameroun-analyse-analyse-ipc-de-la-malnutrition-aigue]"
details: "Le nombre de cas attendus de malnutrition aigu\xEB chez les enfants a \xE9\
  t\xE9 calcul\xE9 \xE0 l'aide de la formule suivante : n*p*k, o\xF9 n est le nombre\
  \ d'enfants de 6-59 projet\xE9 de 2024, p est la pr\xE9valence (MAM ou MAS) de la\
  \ malnutrition aigu\xEB et k est le facteur de correction (incidence 2,6 - MAS et\
  \ 1,5 - MAM). Chez les Femmes Enceintes et Femmes Allaitantes (FEFA) les pr\xE9\
  valences ne sont disponibles que pour les 4 r\xE9gions prioritaires (EN, NO, AD,\
  \ ES) et l'incidence est de k=1."
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC acute malnutrition data collected and classified across 32 departments,
    4 regions, and refugee sites in Cameroon for November 2023 to October 2024. Population
    affected by Global Acute Malnutrition (GAM) and Severe Acute Malnutrition (SAM)
    were assessed using IPC standardized methodology and aggregated by administrative
    and population group boundaries.
  sources:
  - id: source_1
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cameroun-analyse-analyse-ipc-de-la-malnutrition-aigue
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by acute malnutrition (Global Acute Malnutrition
      and Severe Acute Malnutrition) classified by IPC methodology
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Cameroun_Acute_Malnutrition_Nov2023_Oct2024_Report_French.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cameroon - Cameroun : Malnutrition Aigu\xEB (Tableau de population\
    \ de la situation actuelle pour les zones analys\xE9es)"
  download_url: https://data.humdata.org/dataset/8940bf33-e2c3-470e-8ef5-6d90ce71c23c/resource/dbd0c53b-b76c-4e49-ac66-b43455718613/download/cmr-ipc-novembre2023-decembre2024.xlsx
  format: null
  id: resource_dbd0c53b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cmr-ipc-nov2023-dec2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cameroon - Cameroun : Malnutrition Aigu\xEB (Cameroon_Burden et CSL\
    \ 2021)"
  download_url: https://data.humdata.org/dataset/a8a3ea15-527a-425f-b4ea-d421130696cf/resource/fa35bfec-efe6-4b5c-a489-4c4b8191da06/download/cameroon_burden-et-csl-2021.xlsx
  format: null
  id: resource_07a6d31d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Cameroon_Burden et CSL 2021
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmr_hdx_malnutritionaigue_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-10-31'
  start: '2023-01-01'
temporal_resolution: null
title: "Cameroon - Cameroun : Malnutrition Aigu\xEB"
version: null
vulnerability: null
---

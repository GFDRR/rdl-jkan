---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/2022-multi-sectoral-needs-assessment-occupied-palestinian-territory-opt
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/2022-multi-sectoral-needs-assessment-occupied-palestinian-territory-opt
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/2022-multi-sectoral-needs-assessment-occupied-palestinian-territory-opt
dataset_id: rdls_lss-pse_reach_occupiedterritoryopt2022m_2022
description: 'The 2022 Multi-Sector Needs Assessment (MSNA), conducted by the REACH
  Initiative in close collaboration with the United Nations Office for the Coordination
  of Humanitarian Affairs (OCHA), aims to identify and assess multi-sectoral and sector-specific
  needs, circumstances, and vulnerabilities of households across the entirety of the
  Occupied Palestinian Territories (oPt). The assessment is designed to directly inform
  joint humanitarian-development planning across the oPt through the provision of
  comprehensive, multi-sectoral data and inter-sectoral analysis. In particular, the
  MSNA serves as a critical information resource for Humanitarian Program Cycle (HPC)
  activities, principally the development of the Humanitarian Needs Overview (HNO)
  and the Humanitarian Response Plan. All data collection activities for the MSNA
  were conducted by the Palestinian Central Bureau for Statistics (PCBS) and took
  place from May 30 to July 6. A total of 8,331 households were assessed, of which
  4,152 were in the Gaza Strip and 4,179 in the West Bank, including 244 in East Jerusalem.
  Analysis findings at the strata level, meaning the localities of the Gaza Strip,
  the governorates of the West Bank according to ''Oslo Area'', East Jerusalem, and
  H2, are statistically representative with a 95% level of confidence and a +/- 9%
  margin of error. Findings at the governorate level, for both the West Bank and Gaza,
  are representative at a higher degree of accuracy.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/2022-multi-sectoral-needs-assessment-occupied-palestinian-territory-opt]'
details: More information on the methodology can be found in the readme (first sheet
  of the spreadsheet)
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The 2022 MSNA was conducted through a sample survey methodology across
    the Occupied Palestinian Territories by REACH Initiative in collaboration with
    OCHA. The assessment collected multi-sectoral household-level data on needs, vulnerabilities,
    and circumstances to inform humanitarian and development planning across oPt.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2022-multi-sectoral-needs-assessment-occupied-palestinian-territory-opt
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral needs and vulnerabilities of affected households across
      oPt
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the 2022 multisector needs analysis data (MSNA)- a comprehensive
    household-level analysis of all governorates and Oslo areas across the occupied
    Palestinian territory
  download_url: https://data.humdata.org/dataset/f1b3924d-cce7-41fd-9cb3-b838b1224832/resource/b20a072e-f0c2-4200-b54e-bcde69cb422d/download/reach_opt_2022-msna_preliminary_analysis.xlsx
  format: null
  id: resource_b20a072e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_oPt_2022-MSNA_Preliminary_Analysis.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_reach_occupiedterritoryopt2022m_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-07-06'
  start: '2022-05-30'
temporal_resolution: null
title: Palestine - occupied Palestinian territory (oPt) - 2022 Multi-Sectoral Needs
  Assessment
version: null
vulnerability: null
---

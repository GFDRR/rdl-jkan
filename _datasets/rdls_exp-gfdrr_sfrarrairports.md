---
attributions:
- entity:
    affiliation: null
    email: null
    name: RED - Risk, Engineering  Development - Pavia (Italy)
    url: https://www.redrisk.com
  id: CA_SFRARR_RED
  role: principal_investigator
- entity:
    affiliation: null
    email: null
    name: National Institute of Oceanography and Applied Geophysics, OGS, Italy
    url: https://www.ogs.it
  id: CA_SFRARR_OGS
  role: author
- entity:
    affiliation: null
    email: null
    name: World Bank
    url: https://www.worldbank.org
  id: CA_SFRARR_WB
  role: resource_provider
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: paola.ceresa@redrisk.com
  name: Paola Ceresa
  url: null
creator:
  affiliation: null
  email: cscaini@inogs.it
  name: Chiara Scaini
  url: null
dataset_id: rdls_exp-gfdrr_sfrarrairports
description: Location and extent of airports and airstrips across Central Asia (Kazakhstan,
  Kyrgyz Republic, Tajikistan, Turkmenistan, Uzbekistan), compiled under the SFRARR
  program as part of a regionally consistent exposure database.
details: 'Data from the EU-funded ''Strengthening Financial Resilience and Accelerating
  Risk Reduction in Central Asia'' Program (https://www.gfdrr.org/en/program/SFRARR-Central-Asia).
  Exposure data developed using high-resolution global and regional datasets and local
  official data, harmonized to produce a regionally-consistent exposure database for
  Central Asia. The exposure database includes: population, residential buildings,
  non-residential buildings (schools, healthcare facilities, industrial and commercial
  buildings), croplands, transportation system (roads, railways and bridges), airports
  and airstrips, mines, and supply infrastructure. The exposure database developed
  during this project can be used at regional scale, national scale or sub-national
  scale (e.g., at Oblast scale).'
exposure:
- asset_type: null
  category: infrastructure
  id: rdls_exp-gfdrr_sfrarrairports_exp
  metrics:
  - dimension: structure
    id: rdls_exp-gfdrr_sfrarrairports_m1
    measurement:
      quantity_kind: count
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: SFRARR - Strengthening Financial Resilience and Accelerating Risk Reduction
    in Central Asia
  url: https://www.gfdrr.org/en/program/SFRARR-Central-Asia
publisher:
  affiliation: null
  email: null
  name: RED - Risk, Engineering  Development - Pavia (Italy)
  url: https://www.redrisk.com
purpose: Regional risk modelling. These data have been derived on a regional scale
  for the purpose of consistent regional multi-country hazard and risk assessment.
  Application of this information on smaller scales should be done with care. Importantly
  on a local scale, it is often the case that more detailed history and hazard information
  is required to perform such hazard and risk modelling, particularly were applied
  to dimension mitigation structures or strategies., it is often the case that more
  detailed history and hazard information is required to perform such hazard and risk
  modelling, particularly were applied to dimension mitigation structures or strategies
referenced_by:
- author_names: null
  date_published: '2022-11-16'
  doi: null
  id: CA_SFRARR_expReport_EN
  name: Central Asia exposure data development technical report - English version
  url: https://datacatalogfiles.worldbank.org/ddh-published/0064117/DR0091010/Task4_Exposure_Report_r6_EN.pdf?versionId=2023-07-21T17:33:32.2845222Z
- author_names: null
  date_published: '2022-11-16'
  doi: null
  id: CA_SFRARR_expReport_RU
  name: Central Asia exposure data development technical report - Russian version
  url: https://datacatalogfiles.worldbank.org/ddh-published/0064117/DR0091011/Task4_Exposure_Report_r6_RU.pdf?versionId=2023-07-21T17:33:26.6527091Z
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0064255
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Regional layer of airports in Central Asia. The dataset has been developed
    based on global-scale airport layers, and validated locally based on visual inspection.
    The folder contains one points shapefile of the airports locations, and one polygon
    shapefile with the airport extent (assumed based on a circular buffer of variable
    radius). The two shapefiles contain the same fields. These data have been derived
    on a regional scale for the purpose of consistent regional (multi-country hazard
    and risk assessment). Application of this information should on smaller scales
    should be done with care and taking into account the limitations of the approach.
    Files: Airports_Centralasia.shp; Airports_Centralasia_points.shp'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0064255/DR0091666/SFRARR_exposure_CA_Airports.zip?versionId=2023-07-05T13:40:53.8644184Z
  format: shp
  id: rdls_exp-gfdrr_sfrarrairports_r1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Central Asia exposure dataset - airports
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gfdrr_sfrarrairports
spatial:
  bbox:
  - 46.0
  - 34.0
  - 88.0
  - 57.0
  centroid: null
  countries:
  - KAZ
  - KGZ
  - TJK
  - TKM
  - UZB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Central Asia Exposure - Airports (SFRARR)
version: '2022'
vulnerability: null
---

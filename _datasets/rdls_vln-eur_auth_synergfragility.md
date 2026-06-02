---
catalog: null
contact_point:
  email: kpitilak@civil.auth.gr
  id: attribution_contact
  name: Prof. Kyriazis Pitilakis, Aristotle University of Thessaloniki
  url: null
creator:
  email: null
  id: attribution_creator
  name: 'SYNER-G Consortium (14 partners: AUTH, VCE, BRGM, JRC, NGI, UPAV, UROMA,
    METU, AMRA, KIT, UPAT, Willis, UILLINOIS, RCUSS)'
  url: https://cordis.europa.eu/project/id/244061
dataset_id: rdls_vln-eur_auth_synergfragility
description: Seismic fragility functions for European buildings, bridges, utility
  networks (electric power, water, gas), transportation networks (roads, railways),
  and critical facilities (harbors, hospitals) developed under the SYNER-G project
  (EU FP7, Grant No. 244061). The project produced fragility curves for all categories
  of elements at risk using a unified European taxonomy, covering reinforced concrete
  and masonry buildings (5 damage grades DG1-DG5), bridges (yielding and near collapse
  states), utility network components (pipelines, substations, pumping stations),
  road/railway elements (tunnels, embankments, bridge abutments), and critical facilities
  (waterfront structures, cranes, hospital systems). A Fragility Function Manager
  tool was developed for storing, visualizing, harmonizing, and comparing fragility
  functions across different studies. Validated through case studies in Thessaloniki
  (Greece), Vienna (Austria), and multiple Italian sites using Monte Carlo simulation
  with 10,000 runs.
details: 'Fragility functions were derived using analytical methods (nonlinear dynamic
  analysis, 3D FEM, fault tree analysis), empirical methods (post-earthquake damage
  data from Duzce, Lefkas, 1970 Thessaloniki), and hybrid/expert judgement approaches.
  Buildings: RC fragility curves account for shear failure, model uncertainties, and
  scatter of material properties per Eurocode 8; masonry curves use 3D FEM with biaxial
  failure criterion considering in-plane and out-of-plane failure. Bridges: new curves
  for European roadway and railway RC bridges considering bridge length, span count,
  pier characteristics, and seismic design level. Utility networks: empirical and
  analytical fragility relations for individual components (buried pipelines, storage
  tanks, compression stations, pumping stations) with appropriate typology classification,
  damage scale, and intensity measure per component. Transportation: new curves for
  tunnels in alluvial soil, road on embankments/trenches, bridge abutments using PGA.
  Critical facilities: new analytical fragility curves for waterfront/retaining structures
  considering soil-structure response; hospital system fragility using fault tree
  analysis of structural, architectural, and non-structural components. The prototype
  software OOFIMS implements the systemic analysis using Object-Oriented Matlab, integrated
  into the EQvis platform.'
exposure: null
extra_attributions:
- email: null
  id: attribution_funder
  name: European Commission FP7 Programme (Environment, including Climate Change)
  role: funder
  url: https://cordis.europa.eu/project/id/244061
hazard: null
license: open
loss: null
project:
  name: SYNER-G - Systemic Seismic Vulnerability and Risk Analysis (EU FP7, Grant
    No. 244061)
  url: https://cordis.europa.eu/project/id/244061
publisher:
  email: null
  id: attribution_publisher
  name: Aristotle University of Thessaloniki (AUTH)
  url: https://www.auth.gr
purpose: Systemic seismic vulnerability and risk assessment at urban and regional
  level, accounting for inter- and intra-system dependencies between buildings, utility
  networks, transportation networks, and critical facilities. The fragility functions
  enable probabilistic assessment of physical damage, functionality loss, and socio-economic
  impacts from earthquakes across multiple interdependent infrastructure systems.
resources:
- coordinate_system: null
  description: 'SYNER-G fragility functions available through the OpenVulnerability
    platform (Collection #7). The collection contains fragility curves for buildings
    (RC, masonry, DG1-DG5), bridges (yielding/near collapse), utility network components
    (EPN substations/lines, WSS pumping stations/pipelines, GAS pipelines/stations),
    transportation elements (tunnels, embankments, bridge abutments), and critical
    facilities (harbors, hospitals). Original project data documented across seven
    JRC Reference Reports (DOIs: 10.2788/19605 for fragility guidelines, 10.2788/68751
    for taxonomy). The Fragility Function Manager tool is bundled as electronic supplement
    to Springer Book Vol. 27 (DOI: 10.1007/978-94-007-7872-6). Some project deliverable
    PDFs (D3.1, D3.2, D3.5, D3.7, D3.12) remain accessible via VCE archive. The original
    project website (www.syner-g.eu) is offline.'
  download_url: https://openvulnerability.robertogentile.org/products/collection/7
  format: CSV (csv)
  id: resource_synerg_openvulnerability
  media_type: null
  spatial_resolution: null
  temporal: null
  title: SYNER-G Fragility Functions Collection
risk_data_type:
- vulnerability
schema: rdl-03
slug: rdls_vln-eur_auth_synergfragility
spatial:
  countries:
  - AUT
  - GRC
  - ITA
  scale: regional
title: SYNER-G Fragility Functions for Buildings, Lifeline Networks and Infrastructures
version: '1.0'
vulnerability:
  approach: analytical, empirical
  base_data_type: inferred, simulated
  category: buildings, infrastructure
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: earthquake
  hazard_process_primary: ground_motion
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: probability
  relationship: math_parametric
  taxonomy: Custom
  unit: ''
---

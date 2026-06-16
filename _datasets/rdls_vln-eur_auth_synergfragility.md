---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission FP7 Programme (Environment, including Climate Change)
    url: https://cordis.europa.eu/project/id/244061
  id: attribution_funder
  role: funder
catalog: null
contact_point:
  affiliation: null
  email: kpitilak@civil.auth.gr
  name: Prof. Kyriazis Pitilakis, Aristotle University of Thessaloniki
  url: null
creator:
  affiliation: null
  email: null
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
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://cordis.europa.eu/project/id/244061
  rel: source
loss: null
project:
  name: SYNER-G - Systemic Seismic Vulnerability and Risk Analysis (EU FP7, Grant
    No. 244061)
  url: https://cordis.europa.eu/project/id/244061
publisher:
  affiliation: null
  email: null
  name: Aristotle University of Thessaloniki (AUTH)
  url: https://www.auth.gr
purpose: Systemic seismic vulnerability and risk assessment at urban and regional
  level, accounting for inter- and intra-system dependencies between buildings, utility
  networks, transportation networks, and critical facilities. The fragility functions
  enable probabilistic assessment of physical damage, functionality loss, and socio-economic
  impacts from earthquakes across multiple interdependent infrastructure systems.
referenced_by:
- author_names:
  - A. M. Kaynia
  - I. Iervolino
  - F. Taucer
  - U. Hancilar
  date_published: '2013-01-01'
  doi: 10.2788/19605
  id: ref_synerg_report4
  name: 'SYNER-G Reference Report 4: Guidelines for deriving seismic fragility functions
    of elements at risk - Buildings, lifelines, transportation networks and critical
    facilities'
  url: https://publications.jrc.ec.europa.eu/repository/handle/JRC80561
- author_names:
  - P. Franchin
  - A. Elnashai
  - F. Taucer
  - U. Hancilar
  date_published: '2013-01-01'
  doi: 10.2788/69238
  id: ref_synerg_report1
  name: 'SYNER-G Reference Report 1: Methodology for systemic seismic vulnerability
    assessment of buildings, infrastructures, networks and socio-economic impacts'
  url: https://publications.jrc.ec.europa.eu/repository/handle/JRC80613
- author_names:
  - K. Pitilakis
  - H. Crowley
  - A. M. Kaynia
  date_published: '2014-01-01'
  doi: 10.1007/978-94-007-7872-6
  id: ref_springer_vol27
  name: 'SYNER-G: Typology Definition and Fragility Functions for Physical Elements
    at Seismic Risk - Buildings, Lifelines, Transportation Networks and Critical Facilities'
  url: https://link.springer.com/book/10.1007/978-94-007-7872-6
- author_names:
  - K. Pitilakis
  - P. Franchin
  - B. Khazai
  - H. Wenzel
  date_published: '2014-01-01'
  doi: 10.1007/978-94-017-8835-9
  id: ref_springer_vol31
  name: 'SYNER-G: Systemic Seismic Vulnerability and Risk Assessment of Complex Urban,
    Utility, Lifeline Systems and Critical Facilities - Methodology and Applications'
  url: https://link.springer.com/book/10.1007/978-94-017-8835-9
resources:
- access_url: https://openvulnerability.robertogentile.org/products/collection/7
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
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
  download_url: null
  format: null
  id: resource_synerg_openvulnerability
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYNER-G Fragility Functions Collection
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-eur_auth_synergfragility
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - GRC
  - ITA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: SYNER-G Fragility Functions for Buildings, Lifeline Networks and Infrastructures
version: '1.0'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: 'Analytical seismic fragility functions for European RC and
        masonry buildings. RC buildings: fragility curves accounting for shear failure,
        model uncertainties, and material property scatter, following Eurocode 8 assessment.
        Masonry buildings: 3D finite element analysis with nonlinear biaxial failure
        criterion, considering in-plane and out-of-plane failure. Taxonomy: SYNER-G
        building taxonomy based on construction material (RC, masonry), height, design
        code level, and structural system. Validated against damage data from Greek
        earthquakes (1978 Thessaloniki). Intensity measures: PGA (g), Sa(T) (g).'
      approach: analytical
      category: buildings
      damage_scale_name: SYNER-G (DG1-DG5)
      damage_states_names:
      - DG1
      - DG2
      - DG3
      - DG4
      - DG5
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: func_fragility_buildings
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: probability
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    - analysis_details: 'Analytical seismic fragility functions for European roadway
        and railway RC bridges. Parameters: bridge length, number of spans, pier height
        and cross-section, number of columns per pier, seismic design level. Regular
        bridges with continuous deck connected to piers monolithically or through
        elastomeric bearings. Also includes fragility curves for road/railway tunnels
        (alluvial, trench), embankments, and bridge abutments based on numerical analyses
        using PGA. Taxonomy: SYNER-G bridge and transportation taxonomy.'
      approach: analytical
      category: infrastructure
      damage_scale_name: SYNER-G (Yielding/Ultimate)
      damage_states_names:
      - Yielding
      - Near Collapse (Ultimate)
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: func_fragility_transport
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: probability
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    - analysis_details: 'Seismic fragility functions for utility network components:
        electric power network (generators, substations, overhead/underground lines),
        water/wastewater system (pumping stations, water sources, distribution nodes,
        pipelines), and gas network (buried pipelines, storage tanks, compression
        stations, pumping stations). Mostly empirical relations adapted for European
        context. Specific components use fault tree analysis (e.g. Re.Mi cabins, GRF
        Reduction groups in L''Aquila gas network). Also includes harbor components
        (waterfront/retaining structures, cranes) with new analytical fragility curves
        considering soil-structure response, and hospital system components using
        fault tree analysis of structural, architectural, and equipment elements.
        Intensity measures: PGA (g), PGD (m).'
      approach: empirical
      category: infrastructure
      damage_scale_name: SYNER-G (component-specific)
      damage_states_names:
      - Slight
      - Moderate
      - Extensive
      - Complete
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: func_fragility_utilities
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: probability
        modelling: inferred
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    socio_economic: []
    vulnerability: []
---
